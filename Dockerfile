FROM centos:latest

RUN yum -y update
RUN yum -y install epel-release
RUN yum -y install python36 python36-devel python36-setuptools

RUN /usr/local/bin/easy_install-3.6 install pip

RUN adduser bhipwcUser

RUN mkdir /opt/bhiPWC

COPY bhi_pw /opt/bhi_pw
COPY .flaskenv /opt/bhiPWC/
COPY config.py /opt/bhiPWC/
COPY Pipfile /opt/bhiPWC/

RUN /usr/local/bin/pip3 install -r /opt/bhiPWC/Pipfile

CMD ["/usr/local/bin/gunicorn", "--workers", "5", "-b", "127.0.0.1:5000", "/opt/bhiPWC/bhipwc:app"]
