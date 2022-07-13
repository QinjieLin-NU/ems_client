# EMS Client documentation

## APIs in Run.py 

* [run_configurations()](#runconfigurations)

* [get_results()](#getresults)

* [get_best_config()](#getbestconfig)


## APIs in task definition

* [task](#task)
* [report_metric()](#reportmetric)


## APIs in pipeline definition

* [pipeline](#pipeline)
* [create_task()](#createtask)
* [ComputationInstance()](#computationinstance)
* [Dep()](#dep)


## run_configurations()

  Given search space and pipeline DAG, this function runs pipelines paralelly, with each configuration in search space.

  **Usage Syntax**

  ```ruby
  search_space = [ 
  { "params":{"a": 0, "b": 1,}, }, 
  { "params":{"a": 0, "b": 20,}, },
  { "params":{"a": 1, "b": 10,}, },
  ]
  pipeline_dag = "pipeline_v2"

  # Run experiments
  ems.run_configurations(
    pipeline_dag = pipeline_dag,
    search_space = search_space,
  )
  ```

  **Parameter**
    
  * pipeline_dag (string)[Required] 

    The python file name of your pipeline dag definition.

  * search_space (List of Dict)[Required]
    
    The configuration value list. Each element in the list is a dictionay, where the key value is `params`. The `params` maps to a dictionary containing the experimental parameter keys names and values. 

  **Return Type**

    None


### get_results()

### get_best_config()

### task

### report_metric()

### pipeline

### create_task()

### ComputationInstance()

### Dep()


