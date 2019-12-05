apk add zip

# copy source files to a temp directory
cp -a /input/. /copy

# move to folder
cd /copy

# install npm dependencies
npm ci

# zip current folder /copy to archive file in /output folder
zip -r /output/${FILENAME} .