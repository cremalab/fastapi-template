FROM python:3.12
ARG APP_VERSION
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./ /app
RUN echo "${APP_VERSION}" > /app/version.txt
ENV ENVIRONMENT PRODUCTION
ENV PORT 80
EXPOSE 80