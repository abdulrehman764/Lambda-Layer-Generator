# Lambda Layer Generator

This AWS Lambda function is designed to build a custom Lambda Layer by installing a specified Python package and its dependencies, and then uploading it to an S3 bucket. The Lambda Layer can be used in other AWS Lambda functions to easily import and use the installed package.

## Prerequisites

Before using this Lambda function, ensure you have the following prerequisites in place:

1. **AWS Account**: You should have an AWS account with appropriate permissions to create and manage Lambda functions, S3 buckets, and IAM roles.

2. **AWS CLI**: Ensure that the AWS CLI is installed and configured with your AWS credentials.

3. **Python Runtime**: This Lambda function is designed for Python runtime environments.

## Configuration

Follow these steps to configure and deploy the Lambda function:

1. Clone this repository to your local machine or use it directly in your AWS environment.

2. Open the `lambda_function.py` file and configure the Lambda function as follows:

   - Set the `pip_package` variable to the name of the Python package you want to install.
   
   - Optionally, set the `package_version` variable to specify a specific version of the package. If not specified, the latest version will be installed.
   
   - Set the `s3_bucket` variable to the name of your S3 bucket where the Lambda Layer zip file will be uploaded.

3. Deploy the Lambda function to AWS Lambda:

   - You can deploy the Lambda function using the AWS CLI or by packaging and uploading it manually through the AWS Lambda console.

4. Trigger the Lambda function to build the custom Lambda Layer by invoking it:

   - You can manually trigger the Lambda function from the AWS Lambda console or use other methods like AWS Step Functions or CloudWatch Events to automate the process.

5. Once the Lambda function execution is successful, you can find the generated Lambda Layer zip file in your specified S3 bucket. The S3 key for the zip file will include the package name and version (if specified).

6. Use the generated Lambda Layer in your other AWS Lambda functions by including it as a layer in your function configuration.

## Lambda Function Details

- **get_python_version**: This function checks the Python version available in the Lambda runtime environment.

- **install_package**: This function installs the specified Python package and its dependencies in a temporary directory. If a package version is not specified, it installs the latest version.

- **create_zip_archive**: This function creates a zip archive of the installed Python package and its dependencies.

- **upload_to_s3**: This function uploads the zip archive to the specified S3 bucket with a user-defined key.

## Contributing

If you find issues or have improvements to suggest, feel free to open an issue or submit a pull request to this repository.

## Acknowledgments

- This Lambda function was created to simplify the process of creating custom Lambda Layers for Python packages.
