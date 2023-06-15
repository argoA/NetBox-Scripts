from extras.scripts import *

class GetMikroTikInterfaceStatsScript(Script):
  
  class Meta:
    name = "Get MikroTik Interface Stats"
    description = "Pull interface stats for MikroTik devices."
    field_order = ['user', 'password']
    
    user = StringVar(
      description="Username to log into the devices"
    ) 
    
    password = StringVar(
      description="Password to log into the devices"
    )

  def run(self, data, commit):
    self.log_info(f"{data['user']} : {data['password']}")
