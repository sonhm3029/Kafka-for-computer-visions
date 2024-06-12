# How to run

In this project, I use kafka docker image. 

## Tutorial:

[Youtube](https://www.youtube.com/watch?v=Hl61x0s3yeQ&list=PLxoOrmZMsAWxXBF8h_TPqYJNsh3x4GyO4&index=1)

## Environment

- Python=3.9.13

```sh
pip install -r requirements.txt

```

- Install Java if not installed

```sh
sudo apt update
sudo apt install default-jre
java --version
```

## Requirement

- zookeeper -> To manage and run kafka
- kafka
- cmak -> To manage kafka broker, consumer, topic, ... In GUI

## Install Zookeeper and Kafka by hand

## Install Zookeeper and Kafa using docker

The version of Kafka here is: **2.3.0**

```sh
docker-compose up -d
```

## Install CMAK for kafka manager

- Must run in linux

```sh
#clone repo
https://github.com/yahoo/CMAK.git

cd CMAK

./sbt clean dist

cd target/universal/

unzip cmak-xxxx.zip

```

- Config the zookeeper host in cmak-xxxx/conf/application.conf

Change from `cmak.zkhosts="kafka-manager-zookeeper:2181"` to `cmak.zkhosts="<your-ip-addr>:2181"`

In my case i use ipconfig and see that my ip-addr is: 192.168.1.138 like in the `config.py` so my value will be `cmak.zkhosts="192.168.1.138:2181"`

- Run app on port 8080:

```sh
cd cmak-xxxx 
bin/cmak -Dconfig.file=conf/application.conf -Dhttp.port=8080
```

## Run 1 broker, 1 topic, 1 partition, 1 consumer

### Producer

```sh
python test_send.py
```

### Consumer

```sh
python test_receive.py
```