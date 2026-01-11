# Script to organize Python files and push them to GitHub
# This script will:
# 1. Rename all Python files with sequential numbering (01-90)
# 2. Commit each file individually with a clean message (name without number and extension)
# 3. Push all commits to GitHub

# Get all Python files that start with numbers
$files = Get-ChildItem -Path . -Filter "*.py" | Where-Object { $_.Name -match '^\d+' } | Sort-Object { [int]($_.Name -split '_')[0] }

Write-Host "Found $($files.Count) Python files to organize" -ForegroundColor Green

# Create a mapping of old to new filenames
$counter = 1
$renameMap = @()

foreach ($file in $files) {
    $oldName = $file.Name
    
    # Extract the descriptive part (remove number prefix)
    if ($oldName -match '^\d+_(.+)$') {
        $descriptivePart = $matches[1]
    } elseif ($oldName -match '^\d+\s+(.+)$') {
        $descriptivePart = $matches[1]
    } else {
        $descriptivePart = $oldName -replace '^\d+', ''
    }
    
    # Create new filename with sequential number
    $newNumber = "{0:D2}" -f $counter
    $newName = "${newNumber}_${descriptivePart}"
    
    # Extract commit message (remove .py extension)
    $commitMessage = $descriptivePart -replace '\.py$', ''
    
    $renameMap += [PSCustomObject]@{
        OldName = $oldName
        NewName = $newName
        CommitMessage = $commitMessage
        Number = $counter
    }
    
    $counter++
}

# Display the rename plan
Write-Host "`nRename Plan:" -ForegroundColor Cyan
$renameMap | Format-Table -AutoSize

# Ask for confirmation
$confirmation = Read-Host "`nProceed with renaming and pushing? (yes/no)"
if ($confirmation -ne 'yes') {
    Write-Host "Operation cancelled" -ForegroundColor Yellow
    exit
}

Write-Host "`nStarting file organization and git operations..." -ForegroundColor Green

# Phase 1: Rename all files to temporary names to avoid conflicts
Write-Host "`nPhase 1: Renaming to temporary names..." -ForegroundColor Cyan
foreach ($item in $renameMap) {
    $tempName = "temp_${item.Number}_$([System.IO.Path]::GetRandomFileName()).py"
    if (Test-Path $item.OldName) {
        Rename-Item -Path $item.OldName -NewName $tempName -Force
        $item | Add-Member -NotePropertyName TempName -NotePropertyValue $tempName -Force
        Write-Host "  Renamed: $($item.OldName) -> $tempName"
    }
}

# Phase 2: Rename from temporary names to final names
Write-Host "`nPhase 2: Renaming to final sequential names..." -ForegroundColor Cyan
foreach ($item in $renameMap) {
    if ($item.TempName -and (Test-Path $item.TempName)) {
        Rename-Item -Path $item.TempName -NewName $item.NewName -Force
        Write-Host "  Renamed: $($item.TempName) -> $($item.NewName)"
    }
}

Write-Host "`nAll files have been renamed successfully!" -ForegroundColor Green

# Phase 3: Git operations - stage and commit each file
Write-Host "`nPhase 3: Committing files to Git..." -ForegroundColor Cyan

foreach ($item in $renameMap) {
    if (Test-Path $item.NewName) {
        # Stage the file
        git add $item.NewName
        
        # Commit with clean message
        git commit -m "$($item.CommitMessage)"
        
        Write-Host "  Committed: $($item.NewName) with message '$($item.CommitMessage)'" -ForegroundColor Green
    }
}

Write-Host "`nAll files have been committed!" -ForegroundColor Green

# Phase 4: Push to GitHub
Write-Host "`nPhase 4: Pushing to GitHub..." -ForegroundColor Cyan
git push origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "`nSuccessfully pushed all commits to GitHub!" -ForegroundColor Green
} else {
    Write-Host "`nFailed to push to GitHub. Please check your connection and try: git push origin main" -ForegroundColor Red
}

Write-Host "`nOperation complete!" -ForegroundColor Green
