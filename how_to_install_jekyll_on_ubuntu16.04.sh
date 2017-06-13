#!/bin/bash

apt install ruby ruby-dev make gcc g++

gem install bundler
gem install jekyll
gem install jekyll-archives
gem install jekyll-paginate
gem install jekyll-sitemap

# I also used jekyll-related-posts to generate related posts, but..it works but not very good.
apt install zlib1g-dev -y
apt install liblapack-dev -y
gem install jekyll-related-posts

apt install nginx
sed
systemctl restart nginx

git clone https://github.com/silenceshell/silenceshell.github.io.git
cd silenceshell.github.io
jekyll b


