# Databricks notebook source
# DBTITLE 1,Initialize shared context
dbutils.widgets.text(name="en", defaultValue="", label="environment in lower case")
en = dbutils.widgets.get("en")

checkpoint = f"/Volumes/{en}_catalog/silver/checkpoints"
landing = spark.sql('DESCRIBE EXTERNAL LOCATION `landing-gcp-bucket`').select("url").collect()[0][0]
bronze = spark.sql('DESCRIBE EXTERNAL LOCATION `bronze-gcp_bucket`').select("url").collect()[0][0]
silver = spark.sql('DESCRIBE EXTERNAL LOCATION `silve-gcp-bucket`').select("url").collect()[0][0]
gold = spark.sql('DESCRIBE EXTERNAL LOCATION `gold-gcp-bucket`').select("url").collect()[0][0]

print(f"environment: {en}")
print(f"checkpoint: {checkpoint}")
print(f"landing: {landing}")
print(f"bronze: {bronze}")
print(f"silver: {silver}")
print(f"gold: {gold}")

# COMMAND ----------


