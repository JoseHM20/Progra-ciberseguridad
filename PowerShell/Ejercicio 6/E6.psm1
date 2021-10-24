function Ver-StatusPerfil{ 
  param([Parameter(Mandatory)] [Validat("Public", "Private")] [string] $perfil)
      $status = Get-NetFirewallProfile -Name $perfil 
      Write-Host "Perfil:" $perfil 
      if($status.enabled){ 
        Write-Host "Status: Activado" 
        } 
        else{
          Write-Host "Status: Desactivado" 
          }
  }
function Ver-PerfilRedActual{ 
	$perfilRed = Get-NetConnectionProfile 
	Write-Host "El nombre de la red es:" $perfilRed.Name 
	Write-Host "Y su perfil de la red es:" $perfilRed.NetworkCategory 
    }
    
function Test-MrErrorHandling { [CmdletBinding()]
param (
  [Parameter(Mandatory, ValueFromPipeline, ValueFromPipelineByPropertyName)]
  [string[]]$ComputerName) 
  PROCESS {
    foreach ($Computer in $ComputerName) {
      Test-WSMan -ComputerName $Computer
      }
      }
      }
      }
      }
      }


