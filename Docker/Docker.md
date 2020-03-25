# Docker

## Ubuntu安装Docker
### 预安装
> 检查自己的内核版本详细信
```shell script
uname -a

cat /proc/version
```
1. APT镜像源
- 首先需要安装 apt-transport-https 包支持 https 协议的源

    `sudo apt-get install apt-transport-https ca-certificates`

- 添加源的 gpg 密钥
   
   `sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D`

- 获取当前操作系统代号

    `lsb_release -c`
    
- 添加 Docker 的官方 apt 软件源
    
    `trusty: 非 trusty 版本的系统注意修改为自己对应的代号`
    `sudo cat <<EOF > /etc/apt/sources.list.d/docker.list deb https://apt.dockerproject.org/repo ubuntu-trusty main EOF`

- 更新 apt 软件包缓存

    `sudo apt-get update`
    
    