Import-Module Ver-StatusPerfil
function showmenu {
  Clear-Host
  Write-Host "Iniciando programa..." 
  
  Write-Host "1. Ver estatus de conexion" 
  Write-Host "2. Cambiar el estatus de conexion" 
  Write-Host "3. Ver el perfil de nuestra red" 
  Write-Host "4. Cambiar nuestra red a otro perfil" 
  Write-Host "5. Visualizar las reglas de bloqueo" 
  Write-Host "6. Agregar regla de bloqueo extra" 
  Write-Host "7. Eliminar alguna regla de bloqueo" 
  Write-Host "8. Salir del programa"
}

showmenu

do{($respuesta = Read-Host -Prompt "Selecciona una opcion para continuar") -ne 8
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
      Write-Host "Has seleccionado la opcion de cambiar el estatus de los perfiles"
      
      function Editar-StatusPerfil{ 
        param([Parameter(Mandatory)] [ValidateSet("Public","Private")][string] $perfil)
        $status = Get-NetFirewallProfile -Name
        $perfil
        Write-Host "Perfil:" $perfil 
        if($status.enabled){ 
          Write-Host "Status actual: Activado" 
          $opc = Read-Host -Promt "Deseas desactivarlo? [Y] Si [N] No" 
          if ($opc -eq "Y"){ 
            Set-NetFirewallProfile -Name $perfil -Enabled False 
            } 
            } 
            else
            {
              Write-Host "Status: Desactivado" 
              $opc = Read-Host -Promt "Deseas activarlo? [Y] Si [N] No" 
              if ($opc -eq "Y"){ 
                Write-Host "Activando perfil" 
                Set-NetFirewallProfile -Name $perfil -Enabled True 
                } 
                } 
                Ver-StatusPerfil -perfil $perfil
      }
    }

    3{
      Clear-Host
      showmenu
      Write-Host "Has seleccionado la opcion de ver el perfil de la red"
      function Ver-PerfilRedActual{
        $perfilRed = Get-NetConnectionProfile 
        Write-Host "$perfilRed" 
        }  Ver-PerfilRedActual{
     }
    }  
   
    

    4 {
     Clear-Host
     showmenu
    Write-Host "Has seleccionado la opcion de cambiar la red a otro tipo de perfil"

    function Cambiar-PerfilRedActual{ 
      $perfilRed = Get-NetConnectionProfile 
      if($perfilRed.NetworkCategory -eq "Public")
      {
        Write-Host "El perfil actual es público"
        $opc = Read-Host -Prompt "Quieres cambiar a privado? [Y] Si [N] No" 
        if($opc -eq "Y"){ 
          Set-NetConnectionProfile -Name $perfilRed.Name -NetworkCategory Private
         Write-Host "Perfil cambiado" 
		}
    } 
    else
    {
      Write-Host "El perfil actual es privado" 
      $opc = Read-Host -Prompt "Quieres cambiar a público? [Y] Si [N] No" 
      if($opc -eq "Y"){ 
        Set-NetConnectionProfile -Name $perfilRed.Name -NetworkCategory Public
        Write-Host "Perfil cambiado" 
        }
        }
        Ver-PerfilRedActual
        }
    }

   5 {
      Clear-Host
      showmenu
    Write-Host "Has seleccionado la opcion para ver las reglas de bloqueo"
    function Ver-ReglasBloqueo{ 
      if(Get-NetFirewallRule -Action Block -Enabled True -ErrorAction SilentlyContinue){}
        {
          et-NetFirewallRule -Action Block -Enabled True 
    }
       elseif{
          Write-Host "No hay reglas definidas aún"
          
          }
    }
    }
  6 {
      Clear-Host
      showmenu
    Write-Host "Has seleccionado la opcion para agregar una regla de bloqueo a un puerto"
      function Agregar-ReglasBloqueo{ 
	    $puerto = Read-Host -Prompt "Cuál puerto quieres bloquear?" 
	    New-NetFirewallRule -DisplayName "Puerto-Entrada-$puerto" -Profile "Public" -Direction Inbound -Action Block -Protocol TCP -LocalPort $puerto 
        }   
  }  
    
    
   
  
  7 {
      Clear-Host
      showmenu
    Write-Host "Has seleccionado la opcion para eliminar una regla de bloqueo"
    function Eliminar-ReglasBloqueo{ 
	$reglas = Get-NetFirewallRule -Action Block -Enabled True 
	Write-Host "Reglas actuales" 
  foreach($regla in $reglas){ 
    Write-Host "Regla:" $regla.DisplayName 
    Write-Host "Perfil:" $regla.Profile 
    Write-Host "ID:" $regla.Name 
    $opc = Read-Host -Prompt "Deseas eliminar esta regla [Y] Si [N] No" 
    if($opc -eq "Y"){ 
      Remove-NetFirewallRule -ID $regla.name 
      break
      }
      }
      }
    } 

  8 {
    Write-Host "Ha seleccionado la opcion de salir"; break
    
    }
} 
}until($respuesta -gt 7)

