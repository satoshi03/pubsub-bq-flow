# -*- coding:utf-8 -*-

try:
  import setuptools
  from setuptools import setup
except ImportError:
  print("Please install setuptools.")

setup_options = dict(
    name        = "pubsub-bq-flow",
    version     = "0.0.1",
    description = "pubsub to BigQuery via apache beam (cloud dataflow)",
    author      = "satoshi03",
    author_email = "innamisatoshi@gmail.com",
    license     = "MIT",
    url         = "https://github.com/satoshi03/pubsub-bq-flow",
    classifiers = [
      "Programming Language :: Python :: 2.7",
      'License :: OSI Approved :: MIT License'
    ]
    packages    = ['pubsub_bq_flow'],
    package_data = ['config/config.yml']
)

setup(**setup_options)
