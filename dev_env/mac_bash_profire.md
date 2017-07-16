```
# JavaSDK环境配置
export JAVA6_HOME=/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home
export JAVA7_HOME=/Library/Java/JavaVirtualMachines/jdk1.7.0_79.jdk/Contents/Home
export JAVA8_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_91.jdk/Contents/Home
export JAVA_HOME=$JAVA8_HOME
export PATH=$JAVA_HOME/bin:$PATH
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar

# ADB 路径
export PATH=~/Library/Android/sdk/platform-tools/:$PATH

export PATH=~/bin/:$PATH

# NDK环境
export PATH=$PATH:/Users/wangdongdong/env/android-ndk-r12b

#export ANDROID_NDK_ROOT=/Users/wangdongdong/env/android-ndk-r12b
export ANDROID_NDK=/Users/wangdongdong/env/android-ndk-r10e

# gradle环境
export GRADLE_PATH="/Users/wangdongdong/env/gradle-3.4/bin"
export PATH=$PATH:$GRADLE_PATH

##
# Your previous /Users/wangdongdong/.bash_profile file was backed up as /Users/wangdongdong/.bash_profile.macports-saved_2016-06-06_at_15:48:46
##

# MacPorts Installer addition on 2016-06-06_at_15:48:46: adding an appropriate PATH variable for use with MacPorts.
export PATH="/opt/local/bin:/opt/local/sbin:$PATH"
# Finished adapting your PATH environment variable for use with MacPorts.



########################## 自定义别名 alias begin  ######################

#alias subl=\''/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl'\'

alias tree="find . -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'"
# 通过IP连接其他PC
alias gopc="ssh wangdongdong@10.75.75.106"


alias ls="ls"
alias ll="ls -alF"
alias la="ls -A"
alias l="ls -CF"

alias cl="clear"

alias ..="cd .."
alias ...="cd ../.."  
alias ....="cd ../../.."  
alias .....="cd ../../../.."
alias motor="cd /Users/wangdongdong/workingcode/GerritCode/dk/LetvMotor"
alias logs="cd /Users/wangdongdong/logs"

alias vbash="vim /Users/wangdongdong/.bash_profile"
alias sbash="source /Users/wangdongdong/.bash_profile"

alias logcat="echo 'log begin...\n see at /Users/wangdongdong/logs/log.log';adb logcat -c;adb logcat -v time >/Users/wangdongdong/logs/log.log"
alias vlog="open /Users/wangdongdong/logs/log.log"

# git命令简写 
alias gs="git status"
alias gadd="git add app/."
alias gcmt="git commit -s"
alias gamend="git commit --amend"
alias gpush="git push origin master:refs/for/master"
alias gpull="git pull"

##########################  alias end  ######################

# Python环境
# Setting PATH for Python 3.6
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"
export PATH

eval "$(pyenv init -)"
```
