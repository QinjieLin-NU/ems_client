import ems

version_seed = "0001"

@ems.pipeline
def pipeline_flow(pipeline_name):
  """return a List of task"""
  cpu_instance = ems.ComputationInstance(vcpus=15, gpus=0, memory=15)
  gpu_instance = ems.ComputationInstance(vcpus=15, gpus=1, memory=15)

  flow = [
    ems.create_task(name="add", ver=pipeline_name, path="add", computation=cpu_instance, deps={}),
    ems.create_task(name="minus", ver=pipeline_name, path="minus", computation=gpu_instance, 
                    deps={"add": ems.Dep("add"),}),
  ]

  return flow
