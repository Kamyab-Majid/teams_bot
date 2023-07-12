az login
az account set --subscription 8a52a714-5e6b-4d19-aec4-6f1e3829a93e
az identity create --resource-group "AWSDev" --name "searchBotUAM"
az deployment group create --resource-group "AWSDev" --template-file "./deploymentTemplates/template-with-preexisting-rg.json" --parameters appId="83b19eb2-4927-456f-b192-3d2f0d515f33" appType="UserAssignedMSI" tenantId="7f1fcaab-6586-4fac-b4f7-26112c1fd190" existingUserAssignedMSIName="searchBotUAM" existingUserAssignedMSIResourceGroupName="AWSDev" botId="Adastra2023searchBot" newWebAppName="Adastra2023searchBot" newAppServicePlanName="Adastra2023searchBot" appServicePlanLocation="canadacentral" --name "Adastra2023searchBot"
az webapp deployment source config-zip --resource-group "AWSDev" --name "Adastra2023searchBot" --src "teams_bot.zip"