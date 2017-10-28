FROM base

# rubyインストールに必要なパッケージを用意
RUN apt-get update
RUN apt-get install -y --force-yes build-essential curl git zlib1g-dev libssl-dev libreadline-dev libyaml-dev libxml2-dev libxslt-dev

# rbenv, ruby-buildをインストール
RUN git clone https://github.com/sstephenson/rbenv.git /root/.rbenv
RUN git clone https://github.com/sstephenson/ruby-build.git /root/.rbenv/plugins/ruby-build
RUN ./root/.rbenv/plugins/ruby-build/install.sh
ENV PATH /root/.rbenv/bin:$PATH
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh # or /etc/profile
RUN echo 'eval "$(rbenv init -)"' >> .bashrc

# rubyインストール（バージョン指定は ruby-versions.txt に）
ENV CONFIGURE_OPTS --disable-install-doc
ADD ./ruby-versions.txt /root/ruby-versions.txt
RUN xargs -L 1 rbenv install < /root/ruby-versions.txt

# bundlerを各rubyに用意
RUN echo 'gem: --no-rdoc --no-ri' >> /.gemrc
RUN bash -l -c 'for v in $(cat /root/ruby-versions.txt); do rbenv global $v; gem install bundler; done'

# sqlite3をインストール
RUN apt-get install -y sqlite3 libsqlite3-dev

# Node.jsインストール
RUN apt-get install -y software-properties-common
RUN apt-get update
RUN add-apt-repository -y ppa:chris-lea/node.js
RUN echo "deb http://archive.ubuntu.com/ubuntu precise universe" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y nodejs

# ssh準備
RUN mkdir /root/.ssh/

# private keyをコピー
ADD id_rsa /root/.ssh/id_rsa

# known_hosts設定
RUN touch /root/.ssh/known_hosts
# Add bitbuckets key
RUN ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts

# railsアプリケーションをclone
RUN mkdir -p /var/www
RUN git clone git@github.com:k-shogo/rails4-ajax-sample.git /var/www/rails
WORKDIR /var/www/rails

# railsのセットアップ
RUN bash -l -c 'bundle install'
RUN bash -l -c 'bundle exec rake db:create; bundle exec rake db:migrate'
RUN bash -l -c 'bundle exec rake master:import'
ADD ./secrets.yml /var/www/rails/config/secrets.yml

EXPOSE 3000
CMD bash -l -c 'bundle exec rails s'