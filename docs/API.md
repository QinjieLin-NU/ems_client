# EMS Client documentation

## APIs in Run.py 

* [run_configurations()](#runconfigurations)

* [get_results()](#getresults)

* [get_best_config()](#get_bestconfig())


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

  &emsp;None


## get_results()


  Given search space and pipeline DAG, this function return the reported metric in all run pipelines.

  **Usage Syntax**

  ```ruby
  search_space = [ 
  { "params":{"a": 0, "b": 1,}, }, 
  { "params":{"a": 0, "b": 20,}, },
  { "params":{"a": 1, "b": 10,}, },
  ]
  pipeline_dag = "pipeline_v2"

  # Run experiments
  ems.get_results(
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

  &emsp;List of Dict.

  &emsp;**Return Syntax**
  ```ruby
  [{"score":1},{"score":20},{"score":0}]
  ```

## get_best_config()

  Given search space and pipeline DAG, this function return best configuration, with the minimum or maximum reported metric value.

  **Usage Syntax**

  ```ruby
  search_space = [ 
  { "params":{"a": 0, "b": 1,}, }, 
  { "params":{"a": 0, "b": 20,}, },
  { "params":{"a": 1, "b": 10,}, },
  ]
  pipeline_dag = "pipeline_v2"

  # Run experiments
  ems.get_best_config(
    pipeline_dag = pipeline_dag,
    search_space = search_space,
    metric = "score",
    mode = "min",
  )
  ```

  **Parameter**
    
  * pipeline_dag (string)[Required] 

    The python file name of your pipeline dag definition.

  * search_space (List of Dict)[Required]
    
    The configuration value list. Each element in the list is a dictionay, where the key value is `params`. The `params` maps to a dictionary containing the experimental parameter keys names and values. 

  * metric (string)[Required] 

    The key value name of reported metric dictionary in the pipelines.

  * mode (string)[Required] 

    min or max. Currently only support minimum mode and maximum mode.

  **Return Type**

  &emsp;Dict.

  &emsp;**Return Syntax**
  ```ruby
  { "params":{"a": 0, "b": 1,} }
  ```

## report_metric()

  Report metric in the task. For example, developer can report training loss in training loops.

  **Usage Syntax**

  ```ruby
  @ems.task
  def main(config, args):
    a = config.params.a
    b = config.params.b
    score = a ** 2 + b

    ems.report_metric(
      report_result={"score":score},
      result_path=args.config_result_path
    )
    return 

  if __name__ == "__main__":
    main()
  ```

  **Parameter**
    
  * report_result (Dict)[Required] 

    A dictionary of reported keys and values. 

  * result_path (String)[Required]
    
    A file path, given from `args` input.

  **Return Type**

  &emsp;None

## ComputationInstance()

  Computation resource specification. It contain cpu number, gpu number and memory size.

  **Usage Syntax**

  ```ruby
  gpu_instance = ems.ComputationInstance(vcpus=15, gpus=1, memory=15)
  ```

  **Parameter**
    
  * vcpus (Int)[Required] 

    The number of cpu.

  * gpus (Int)[Required]
    
    The number of the gpu.

  * memory (Int)[Required]
    
    The memory size, based on Gi. 

  **Return Type**

  &emsp;ems.ComputationInstance


## create_task()

  Create a task in the pipeline flow. Developer can specify the executed module name, version number, task dependency and computation resource. 

  **Usage Syntax**

  ```ruby
  cpu_instance = ems.ComputationInstance(vcpus=15, gpus=0, memory=15)
  
  flow = [ems.create_task(name="add", ver=pipeline_name, 
    path="add", computation=cpu_instance, deps={}),]
  ```

  **Parameter**
    
  * name (String)[Required] 

    Name of the task. It is used when specifying depdendency.

  * ver (String)[Required] 

    A version string of the task. It can be `pipeline_name`. For example, if task is for training model and evaluating model, it would better be  `pipeline_name`. If given a random string, it means the task is shared among different pipelines. For example, if preprocess task is preprocessing the same raw data for all pipeline, it should be executed once and preprocess resulted can be used for all other pipelines. Then the `ver` of this task can be a random string but not `pipeline_name`.

  * path (String)[Required] 

    The file path to an executable python module. The path should be relative path to the `tasks` folder. 

  * computation (ComputationInstance)[Required]
    
    The computation resource including cpu number, gpu number and memory size for the task.

  * deps (Dict)[Required]
    
    The dependency of the task. For example,`deps={"train": ems.Dep("mnist/train"),})`.

  **Return Type**

  &emsp;ems.Task, but not ems.task decrator.


## Dep()

  A task Dependency. It should be used in the create_task() function.

  **Usage Syntax**

  ```ruby
  ems.create_task(name="mnist/train", ver=pipeline_name, path="mnist/train", 
      computation=gpu_instance, deps={}),
  ems.create_task(name="mnist/eval", ver=pipeline_name, path="mnist/eval", 
      computation=gpu_instance, deps={"train": ems.Dep("mnist/train"),}),
  ```

  **Parameter**
    
  * name (string)[Required] 

    The name of the dependency task.

  **Return Type**

  &emsp;ems.Dep


## task

## pipeline
