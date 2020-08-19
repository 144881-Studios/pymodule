1. Create a branch from “_template_” and publish module(s) in releases' branch.
2. Try to download it and get the download link.
3. From your branch,create a pull request of the page in pymodule/module/module-name/README.md (there is a template and you don't need create it again):
3. From the branch,create a pull request of the page in pymodule/module/module-name/README.md :
```markdown
# module_name
by auther_name
## Latest Release
### version [latest_file_name](download_link)\(publish_time\)  
[**View all of this release**](github_release_link)
#### version [older_file_name](download_link)\(publish_time\)  
[View all of this release](github_release_link)
version [**another_older_file_name**](download_link)\(publish_time\)  
[View all of this release](github_release_link)
version [**another_older_file_name_else**](download_link)\(publish_time\)  
[View all of this release](github_release_link)
```
4. Wait for managers to audit.
5. File automatically merged to the master branch,and it will show in the site.