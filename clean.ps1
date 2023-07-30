##########################################################################################
# FILE: clean.ps1                                                                         
# PROJECT: Standalone Script                                                              
# PURPOSE: This Script automates the following for directory from which it is run:        
#   1. Check the directory and all subdirectories for the listed objects to delete        
#   2. After user confirmation, recursively delete all listed paths                       
# BEFORE RUNNING: Make sure to define the following variables below:                      
#   - $ITEMS_TO_DELETE: The objects to delete throughout the directory and subdirectories 
# PARAMETERS: NONE                                                                        
# EXAMPLE CALL:                                                                           
#   - Make sure to call this script from the project root directory from Powershell:      
#       > ./clean.ps1                                                                     
##########################################################################################
# 1.0.0     2023/03/22      Maeva Ralafiarindaza    : INITIAL RELEASE                     
##########################################################################################
# ACTION ITEM: List all the objects to delete throughout the directory and subdirectories
$ITEMS_TO_DELETE = @('__pycache__','.mypy_cache','.pyc')
##########################################################################################

# Variables
$paths_to_delete = [System.Collections.ArrayList]@()

# Check for all the elements-to-delete through the entire directory and subdirectories
# Get their full-paths
foreach ($item in $ITEMS_TO_DELETE)
{
    # Get all the objects that match the name of the item
    $objs = $(Get-ChildItem -Path . -Filter $item -Recurse -ErrorAction SilentlyContinue -Force)

    # If multiple objects are found, loop through them and append their fullpath to the $paths_to_delete
    if ($objs.Length -gt 0) 
    {
        foreach ($obj in $objs) 
        {
            $Null = $paths_to_delete.Add($obj.FullName)
        }
    }
    else # Found only one object: Append its fullpath directly
    {
        $Null = $paths_to_delete.Add($objs.FullName)
    }
}

# Here, $objs_to_delete may contain file or folder objects, or nothing found
if ($paths_to_delete.Length -gt 0) 
{
    # Get confirmation from user about the items to be deleted
    Write-Host ""
    Write-Host "The following items will be deleted:"
    foreach ($path in $paths_to_delete)
    {
        Write-Host "`t$($path)"
    }
    Write-Host ""
    $confirm = Read-Host -Prompt "Do you want to continue? (Enter 'y' to confirm, else aborting)"

    # Depending on the user's input, we might delete or not
    if (($confirm -eq 'y') -or ($confirm -eq 'Y'))
    {
        Write-Host "Deleting..."
        foreach ($path in $paths_to_delete)
        {
            if ($path -ne $Null)
            {
                Remove-Item -Recurse -Force $path
            }
        }
        Write-Host "Files have been removed."
        exit
    }
    else
    {
        Write-Host "Aborting..."
        exit
    }
}
else
{
    Write-Host "No objects to delete found."
    exit
}