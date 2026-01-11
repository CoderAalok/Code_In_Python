# Script to push remaining uncommitted files
# 1. Commit deletions/modifications
# 2. Commit untracked files individually

# Stage deleted/modified files
git add -u
if ((git status --porcelain -uno).Length -gt 0) {
    git commit -m "Sync_deletions_and_modifications"
    Write-Host "Committed deletions/modifications" -ForegroundColor Green
}

# Get untracked files, exclude pycache
$untracked = git status --porcelain | Where-Object { $_ -match '^\?\?' } | ForEach-Object { $_.Substring(3) } | Where-Object { $_ -notmatch '__pycache__' }

foreach ($file in $untracked) {
    # Trim quotes if present (git status might quote filenames with spaces)
    $cleanPath = $file.Trim('"')
    
    if (Test-Path $cleanPath) {
        $name = [System.IO.Path]::GetFileNameWithoutExtension($cleanPath)
        
        git add $cleanPath
        git commit -m "$name"
        Write-Host "Committed $cleanPath as '$name'" -ForegroundColor Green
    }
}

# Push
git push origin main
Write-Host "All changes pushed to GitHub" -ForegroundColor Green
