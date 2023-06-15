from extras.scripts import *
from dcim.models import Device

class GetMikroTikInterfaceStatsScript(Script):
  
    class Meta:
        name = "Get MikroTik Interface Stats"
        description = "Pull interface stats for MikroTik devices."
        field_order = ['user', 'password', 'site']
    
    user = StringVar(
        description="Username used to log into the devices"
    )
    password = StringVar(
        description="Password used to log into the devices"
    )
    site = ObjectVar(
        description="Site of the device",
        
    )

    def run(self, data, commit):
        
        # Get a list of MikroTik routers
        for device in Device.objects.filter(site=data['site']):
            self.log_success(device)
