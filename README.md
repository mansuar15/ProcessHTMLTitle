<!--
title: 'Process HTML Title in Python'
description: 'This example demonstrates how to extract the title tag of a HTML document as response to a petition.'
layout: Doc
framework: v1
platform: AWS
language: Python
authorLink: 'https://github.com/mansuar15'
authorName: 'Manuel Suárez'
-->
# Process HTML Title in Python

This example demonstrates how to extract the title tag of a HTML document as response to a petition.

## Deploy

Endpoints:
```bash
GET - https://6wp5fr5735.execute-api.us-east-1.amazonaws.com/dev/getTitle
```
Example:

```bash
serverless invoke -f getTitle -d www.google.com
```