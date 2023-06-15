from extras.scripts import *
from dcim.models import Device

class GetMikroTikInterfaceStatsScript(Script):
  
  class Meta:
    name = "Get MikroTik Interface Stats"
    description = "Pull interface stats for MikroTik devices."
    field_order = ['user', 'password']
    
  user = StringVar(
    description="Username used to log into the devices"
  )
  password = StringVar(
    description="Password used to log into the devices"
  )

  def run(self, data, commit):
    for device in Device.objects.filter(name='Testing-Router'):
      self.log_success(device)
