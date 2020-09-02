# Module Publishing Guidelines
For module name,if it is a Windows version,the module name must be 2~8 letters.
## How to publish a module
### 1.Apply for a contributor.
**Don't have a GitHub account?[Sign in](https://github.com) or [Email to us to publish a module](mailto:cyy144881@icloud.com?subject=PyModule%3a%20module_name)**
### 2.Create a branch from “\_template\_” and publish Module(s) in releases branch.
### 3.Try to download it and get the download link.
### 4.From your branch,create a pull request of the page in pymodule/module/module-name/README.md :
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
### 5.Wait for audit.
### 6.File automatically merged to the master branch,and it will show in the site.
## Version tag
### Commit of 144881 Studios,the vertion tag allows“v=a.b.c.dec;b<=a+9;”rule.  
### Commit of others,can create your rules.
## File name
### A good file name might be 'module\_name'+'version\_tag'+'python\_ver'.
## Python 2.x versions
### If you want to publish a release of Python 2.x versions,please add '\(2.x\)' to the branch name.
#### \(Except this module can be used either in Python 2.x and Python 3.x.\)
[Module home page](https://144881-studios.github.io/pymodule/module)  
[Search a module](https://144881-studios.github.io/pymodule/search)  
[Email to us](mailto:cyy144881@icloud.com?subject=PyModule)
