import E6.psm1

# Autores
# Jose Luis Hernandez Meza
# Gerardo Gamez Serna 
# Francisco Javier Valerio Lara

function showmenu {
  Clear-Host
  Write-Host "Iniciando programa..." 
  
  Write-Host "1. Ver estatus de conexion" 
  Write-Host "2. Ver el perfil de nuestra red"
  Write-Host "3. Existencia de errores" 
  }


showmenu

do {($respuesta = Read-Host -Prompt "Selecciona una opcion para continuar") -ne 2

  switch ($respuesta)

 {
    1{
      Clear-Host
      showmenu
      Write-Host "Has seleccionado la opcion para ver estatus de conexion"
      function Ver-StatusPerfil{ param([Parameter(Mandatory)] [Validat("Public", "Private")] [string] $perfil)
      $status = Get-NetFirewallProfile Write-Host "Status": $status
      }
      Write-Host "Perfil:" $perfil 
      if($status.enabled){
        Write-Host "Status: Activado"
        }
        else{
          Write-Host "Status: Desactivado"
          }
          }
    2{
      Clear-Host
      showmenu
      Write-Host "Has seleccionado la opcion de ver el perfil de la red"
      function Ver-PerfilRedActual{
        $perfilRed = Get-NetConnectionProfile 
        Write-Host "Su perfil es:" $perfilRed
        }
        Ver-PerfilRedActual{}
        }

    3{
      
      showmenu
      Write-Host "Has seleccionado la opcion de verificar errores de codigo"
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
until($respuesta -gt 3)

