# pymodule
Commit some Python modules.
# Module Publishing Guidelines
For module name,if it is a Windows version,the module name must be 2~8 letters.
## How to publish a module
### 1.Create a branch and publish Module in releases branch.
### 2.Try to download it and get the download link.
### 3.From the branch,create a pull request of the page in pymodule/module/module-name/README.md :
```markdown
# module_name
by auther_name
## Latest Release
### [latest_file_name](download_link)\(publish_time\)  
[**View all of this release**](github_release_link)
#### [older_file_name](download_link)\(publish_time\)  
[View all of this release](github_release_link)
[**another_older_file_name**](download_link)\(publish_time\)  
[View all of this release](github_release_link)
[**another_older_file_name_else**](download_link)\(publish_time\)  
[View all of this release](github_release_link)
```
### 4.Wait for audit.
## Version tag
### Commit of 144881 Studios,the vertion tag allows“v=a.b.c.dec;b<=a+9;”rule.  
### Commit of others,can create your rules.
[Home page](https://144881-studios.github.io/pymodule/module)
