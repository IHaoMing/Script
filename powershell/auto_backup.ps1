$source_path = "E:\code\Script"

$destination_home = "E:\backup"
$destination_path = $destination_home + "\" + (Get-Date).ToString("yyyyMMdd")

#目标路径不存在，则新建路径
if(!(Test-Path -Path $destination_path))
{
    New-Item -ItemType directory -Path $destination_path
}

foreach($Path in $source_path)
{
    Copy-Item -Path $Path -Destination $destination_path -Recurse -Force
}