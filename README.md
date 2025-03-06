# multi_repo_golden_image


 curl -X POST \
  -H "Accept: application/vnd.github.everest-preview+json" \
  -H "Authorization: token <TOKEN>" \
  -d '{
        "event_type": "main-update",
        "client_payload": {
          "component": "main",
          "version": "2.0.1"
        }
      }' \
  https://api.github.com/repos/hemanthsagarb9/multi_repo_golden_image/dispatches
