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
## File name
### A good file name might be 'module_name'+'version_tag'+'python_ver'.
## Python 2.x versions
### If you want to publish a release of Python 2.x versions,please add '\(2.x\)' to the branch name.
#### \(Except this module can be used either Python 2.x and Python 3.x.\)
[Module home page](https://144881-studios.github.io/pymodule/module)  
[Email to us](mailto:cyy144881@icloud.com?subject=PyModule)
