# Crear un archivo en el escritorio
$desktopPath = [Environment]::GetFolderPath("Desktop")
$filePath = Join-Path $desktopPath "example_file.txt"
"Este es un archivo creado por PowerShell." | Out-File -FilePath $filePath
