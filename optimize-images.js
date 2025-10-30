#!/usr/bin/env node

/**
 * Image Optimization Script for Trilink Site
 *
 * This script optimizes all JPG, JPEG, and PNG images in the static/images directory
 * by resizing them to appropriate dimensions and compressing them for web use.
 *
 * Features:
 * - Resizes hero images to max 1920x1080 (maintaining aspect ratio)
 * - Resizes service images to max 1920x1080
 * - Resizes badges/icons to max 800x800
 * - Compresses JPG images to quality 85
 * - Compresses PNG images with optimal compression
 * - Creates backups in static/images/originals/ before optimization
 * - Provides detailed before/after statistics
 *
 * Usage:
 *   node optimize-images.js           # Optimize all images
 *   node optimize-images.js --dry-run # Preview what would be optimized
 *   node optimize-images.js --restore # Restore from backups
 */

const sharp = require('sharp');
const fs = require('fs').promises;
const path = require('path');

// Configuration
const CONFIG = {
  imageDir: path.join(__dirname, 'static', 'images'),
  backupDir: path.join(__dirname, 'static', 'images', 'originals'),

  // Size limits for different image types
  sizes: {
    hero: { width: 1920, height: 1080 },
    service: { width: 1920, height: 1080 },
    badge: { width: 800, height: 800 },
    icon: { width: 800, height: 800 },
    default: { width: 1920, height: 1080 }
  },

  // Quality settings
  quality: {
    jpg: 85,
    png: 90,
    webp: 85
  },

  // Minimum file size to optimize (in bytes)
  minFileSize: 50 * 1024, // 50KB
};

// Parse command line arguments
const args = process.argv.slice(2);
const isDryRun = args.includes('--dry-run');
const isRestore = args.includes('--restore');
const verbose = args.includes('--verbose') || args.includes('-v');

// Statistics
const stats = {
  totalFiles: 0,
  optimizedFiles: 0,
  skippedFiles: 0,
  totalSizeBefore: 0,
  totalSizeAfter: 0,
  errors: []
};

/**
 * Get all image files recursively
 */
async function getImageFiles(dir, fileList = []) {
  const files = await fs.readdir(dir);

  for (const file of files) {
    const filePath = path.join(dir, file);
    const stat = await fs.stat(filePath);

    if (stat.isDirectory()) {
      // Skip backup directory
      if (filePath !== CONFIG.backupDir) {
        await getImageFiles(filePath, fileList);
      }
    } else {
      // Check if it's an image file
      const ext = path.extname(file).toLowerCase();
      if (['.jpg', '.jpeg', '.png'].includes(ext)) {
        fileList.push(filePath);
      }
    }
  }

  return fileList;
}

/**
 * Determine optimal size for image based on its location
 */
function getOptimalSize(filePath) {
  const relativePath = path.relative(CONFIG.imageDir, filePath).toLowerCase();

  if (relativePath.includes('heroes')) {
    return CONFIG.sizes.hero;
  } else if (relativePath.includes('services')) {
    return CONFIG.sizes.service;
  } else if (relativePath.includes('badges')) {
    return CONFIG.sizes.badge;
  } else if (relativePath.includes('icons')) {
    return CONFIG.sizes.icon;
  }

  return CONFIG.sizes.default;
}

/**
 * Create backup of original file
 */
async function createBackup(filePath) {
  const relativePath = path.relative(CONFIG.imageDir, filePath);
  const backupPath = path.join(CONFIG.backupDir, relativePath);
  const backupDir = path.dirname(backupPath);

  // Create backup directory if it doesn't exist
  await fs.mkdir(backupDir, { recursive: true });

  // Copy original file to backup
  await fs.copyFile(filePath, backupPath);

  if (verbose) {
    console.log(`  ✓ Backup created: ${path.relative(__dirname, backupPath)}`);
  }
}

/**
 * Optimize a single image
 */
async function optimizeImage(filePath) {
  try {
    const stat = await fs.stat(filePath);
    const originalSize = stat.size;

    // Skip small files
    if (originalSize < CONFIG.minFileSize) {
      if (verbose) {
        console.log(`  ⊘ Skipping (< 50KB): ${path.relative(__dirname, filePath)}`);
      }
      stats.skippedFiles++;
      return;
    }

    stats.totalFiles++;
    stats.totalSizeBefore += originalSize;

    const ext = path.extname(filePath).toLowerCase();
    const optimalSize = getOptimalSize(filePath);

    console.log(`\n📸 Processing: ${path.relative(__dirname, filePath)}`);
    console.log(`  Original size: ${(originalSize / 1024).toFixed(2)} KB`);

    if (isDryRun) {
      console.log(`  Would optimize to max ${optimalSize.width}x${optimalSize.height}`);
      stats.optimizedFiles++;
      return;
    }

    // Create backup before optimization
    await createBackup(filePath);

    // Load image with sharp
    const image = sharp(filePath);
    const metadata = await image.metadata();

    console.log(`  Current dimensions: ${metadata.width}x${metadata.height}`);

    // Resize if needed
    let pipeline = image.resize(optimalSize.width, optimalSize.height, {
      fit: 'inside',
      withoutEnlargement: true
    });

    // Apply compression based on format
    if (['.jpg', '.jpeg'].includes(ext)) {
      pipeline = pipeline.jpeg({
        quality: CONFIG.quality.jpg,
        progressive: true,
        mozjpeg: true
      });
    } else if (ext === '.png') {
      pipeline = pipeline.png({
        quality: CONFIG.quality.png,
        compressionLevel: 9,
        adaptiveFiltering: true
      });
    }

    // Save optimized image
    await pipeline.toFile(filePath + '.tmp');

    // Replace original with optimized
    await fs.unlink(filePath);
    await fs.rename(filePath + '.tmp', filePath);

    // Get new file size
    const newStat = await fs.stat(filePath);
    const newSize = newStat.size;
    const savings = originalSize - newSize;
    const savingsPercent = ((savings / originalSize) * 100).toFixed(1);

    stats.totalSizeAfter += newSize;
    stats.optimizedFiles++;

    console.log(`  Optimized size: ${(newSize / 1024).toFixed(2)} KB`);
    console.log(`  ✓ Saved: ${(savings / 1024).toFixed(2)} KB (${savingsPercent}%)`);

  } catch (error) {
    console.error(`  ✗ Error: ${error.message}`);
    stats.errors.push({ file: filePath, error: error.message });
  }
}

/**
 * Restore images from backup
 */
async function restoreFromBackup() {
  console.log('🔄 Restoring images from backup...\n');

  try {
    const backupExists = await fs.access(CONFIG.backupDir).then(() => true).catch(() => false);

    if (!backupExists) {
      console.log('❌ No backup directory found. Nothing to restore.');
      return;
    }

    const backupFiles = await getImageFiles(CONFIG.backupDir);

    for (const backupPath of backupFiles) {
      const relativePath = path.relative(CONFIG.backupDir, backupPath);
      const originalPath = path.join(CONFIG.imageDir, relativePath);

      await fs.copyFile(backupPath, originalPath);
      console.log(`✓ Restored: ${relativePath}`);
    }

    console.log(`\n✅ Restored ${backupFiles.length} images from backup.`);

  } catch (error) {
    console.error(`❌ Error restoring backup: ${error.message}`);
  }
}

/**
 * Print summary statistics
 */
function printSummary() {
  console.log('\n' + '='.repeat(60));
  console.log('📊 OPTIMIZATION SUMMARY');
  console.log('='.repeat(60));

  if (isDryRun) {
    console.log('\n⚠️  DRY RUN MODE - No files were modified\n');
  }

  console.log(`Total images found: ${stats.totalFiles}`);
  console.log(`Images optimized: ${stats.optimizedFiles}`);
  console.log(`Images skipped: ${stats.skippedFiles}`);

  if (stats.totalSizeBefore > 0) {
    const totalSavings = stats.totalSizeBefore - stats.totalSizeAfter;
    const totalSavingsPercent = ((totalSavings / stats.totalSizeBefore) * 100).toFixed(1);

    console.log(`\nTotal size before: ${(stats.totalSizeBefore / 1024 / 1024).toFixed(2)} MB`);
    console.log(`Total size after: ${(stats.totalSizeAfter / 1024 / 1024).toFixed(2)} MB`);
    console.log(`Total saved: ${(totalSavings / 1024 / 1024).toFixed(2)} MB (${totalSavingsPercent}%)`);
  }

  if (stats.errors.length > 0) {
    console.log('\n⚠️  Errors encountered:');
    stats.errors.forEach(({ file, error }) => {
      console.log(`  ✗ ${path.relative(__dirname, file)}: ${error}`);
    });
  }

  console.log('\n' + '='.repeat(60));

  if (!isDryRun && stats.optimizedFiles > 0) {
    console.log('\n💾 Original files backed up to: static/images/originals/');
    console.log('   To restore, run: node optimize-images.js --restore');
  }
}

/**
 * Main execution
 */
async function main() {
  console.log('🖼️  Trilink Site - Image Optimization Tool\n');

  if (isRestore) {
    await restoreFromBackup();
    return;
  }

  if (isDryRun) {
    console.log('⚠️  DRY RUN MODE - No files will be modified\n');
  }

  console.log('Configuration:');
  console.log(`  Hero images: max ${CONFIG.sizes.hero.width}x${CONFIG.sizes.hero.height}`);
  console.log(`  Service images: max ${CONFIG.sizes.service.width}x${CONFIG.sizes.service.height}`);
  console.log(`  Badges/Icons: max ${CONFIG.sizes.badge.width}x${CONFIG.sizes.badge.height}`);
  console.log(`  JPG Quality: ${CONFIG.quality.jpg}`);
  console.log(`  PNG Quality: ${CONFIG.quality.png}`);
  console.log(`  Min file size: ${CONFIG.minFileSize / 1024} KB\n`);

  const imageFiles = await getImageFiles(CONFIG.imageDir);

  console.log(`Found ${imageFiles.length} images to process.\n`);

  for (const filePath of imageFiles) {
    await optimizeImage(filePath);
  }

  printSummary();
}

// Run the script
main().catch(error => {
  console.error('Fatal error:', error);
  process.exit(1);
});
