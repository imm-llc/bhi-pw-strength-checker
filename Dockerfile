FROM centos:latest

RUN yum -y update
RUN yum -y install epel-release
RUN yum -y install python36 python36-devel python36-setuptools

RUN /usr/bin/easy_install-3.6 pip

ADD bhi_pw /bhi_pw
COPY .flaskenv /
COPY config.py /
COPY Pipfile /

RUN /usr/local/bin/pip3 install -r /Pipfile

WORKDIR /
CMD ["/usr/local/bin/gunicorn", "--workers", "5", "-b", "0.0.0.0:5000", "bhi_pw:app"]
