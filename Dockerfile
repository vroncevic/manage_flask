# Copyright 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

FROM debian:12
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get install -yq --no-install-recommends \
    vim \
    nano \
    tree \
    htop \
    wget \
    curl \
    unzip \
    ca-certificates \
    openssl \
    python3 \
    python3-dev \
    python3-pip \
    python3-wheel

RUN pip3 install --upgrade setuptools
COPY requirements.txt /
RUN pip3 install -r requirements.txt
RUN rm -f requirements.txt
RUN mkdir /manage_commands/
COPY manage_commands /manage_commands/
COPY manage.py /
RUN find /manage_commands/ -name "*.editorconfig" -type f -exec rm -Rf {} \;
RUN mkdir /FlaskApp/
RUN mv manage.py /FlaskApp/
RUN mv /manage_commands/ /FlaskApp/
RUN rm -rf /manage_commands/
RUN chmod -R 755 /FlaskApp/
RUN tree /FlaskApp/

