from extras.scripts import *
from dcim.models import Device, DeviceType, Manufacturer

import routeros_api

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
    for device in Device.objects.get(name="Test-Router"):
      self.log_info(device)
