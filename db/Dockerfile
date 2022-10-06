FROM mongo

LABEL "com.project.author"="Walther" version="0.1"

EXPOSE 27017/tcp

HEALTHCHECK --interval=5m --timeout=3s CMD curl -f mongodb://localhost:27017 || exit 1
