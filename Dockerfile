FROM 343548683418.dkr.ecr.us-east-1.amazonaws.com/ecommerce_api:2021.01.01_latest as last-build

FROM 343548683418.dkr.ecr.us-east-1.amazonaws.com/python_development_base:ubuntu-latest

COPY --chown=cashstar:cashstar --from=last-build /opt/cashstar /opt/cashstar

ENV APPLICATION_NAME ecommerce_api
ENV APPLICATION_DIR /opt/cashstar/app/$APPLICATION_NAME
ENV MANAGE_PY_LOCATION $APPLICATION_DIR/$APPLICATION_NAME

WORKDIR $APPLICATION_DIR

ENTRYPOINT ["/opt/cashstar/app/ecommerce_api/docker/entrypoint.dev.sh"]

