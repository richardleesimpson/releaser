#
FROM python:3-onbuild

#
COPY config.json ./

#
CMD ["python", "releaser.py"]