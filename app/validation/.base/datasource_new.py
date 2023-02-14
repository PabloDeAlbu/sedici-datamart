#!/usr/bin/env python
# coding: utf-8

# # Create a new pandas Datasource
# Use this notebook to configure a new pandas Datasource and add it to your project.

# In[ ]:


import great_expectations as gx
from great_expectations.cli.datasource import sanitize_yaml_and_save_datasource, check_if_datasource_name_exists
context = gx.get_context()


# ## Customize Your Datasource Configuration
# 
# **If you are new to Great Expectations Datasources,** you should check out our [how-to documentation](https://docs.greatexpectations.io/docs/guides/connecting_to_your_data/connect_to_data_overview)
# 
# **My configuration is not so simple - are there more advanced options?**
# Glad you asked! Datasources are versatile. Please see our [How To Guides](https://docs.greatexpectations.io/docs/guides/connecting_to_your_data/connect_to_data_overview)!
# 
# Give your datasource a unique name:

# In[ ]:


datasource_name = "my_datasource"


# ### For files based Datasources:
# Here we are creating an example configuration.  The configuration contains an **InferredAssetFilesystemDataConnector** which will add a Data Asset for each file in the base directory you provided. It also contains a **RuntimeDataConnector** which can accept filepaths.   This is just an example, and you may customize this as you wish!
# 
# Also, if you would like to learn more about the **DataConnectors** used in this configuration, including other methods to organize assets, handle multi-file assets, name assets based on parts of a filename, please see our docs on [InferredAssetDataConnectors](https://docs.greatexpectations.io/docs/guides/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector) and [RuntimeDataConnectors](https://docs.greatexpectations.io/docs/guides/connecting_to_your_data/how_to_configure_a_runtimedataconnector).
# 

# In[ ]:


example_yaml = f"""
name: {datasource_name}
class_name: Datasource
execution_engine:
  class_name: PandasExecutionEngine
data_connectors:
  default_inferred_data_connector_name:
    class_name: InferredAssetFilesystemDataConnector
    base_directory: ../data
    default_regex:
      group_names:
        - data_asset_name
      pattern: (.*)
  default_runtime_data_connector_name:
    class_name: RuntimeDataConnector
    assets:
      my_runtime_asset_name:
        batch_identifiers:
          - runtime_batch_identifier_name
"""
print(example_yaml)


# # Test Your Datasource Configuration
# Here we will test your Datasource configuration to make sure it is valid.
# 
# This `test_yaml_config()` function is meant to enable fast dev loops. **If your
# configuration is correct, this cell will show you some snippets of the data
# assets in the data source.** You can continually edit your Datasource config
# yaml and re-run the cell to check until the new config is valid.
# 
# If you instead wish to use python instead of yaml to configure your Datasource,
# you can use `context.add_datasource()` and specify all the required parameters.

# In[ ]:


context.test_yaml_config(yaml_config=example_yaml)


# ## Save Your Datasource Configuration
# Here we will save your Datasource in your Data Context once you are satisfied with the configuration. Note that `overwrite_existing` defaults to False, but you may change it to True if you wish to overwrite. Please note that if you wish to include comments you must add them directly to your `great_expectations.yml`.

# In[ ]:


sanitize_yaml_and_save_datasource(context, example_yaml, overwrite_existing=False)
context.list_datasources()


# Now you can close this notebook and delete it!
