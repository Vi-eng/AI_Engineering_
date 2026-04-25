//package org.example;

package org.example;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
        import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.Map;

@RestController
@CrossOrigin(origins = "*")
@RequestMapping("/api/assistant")
public class AssistantController {

    private final RestTemplate restTemplate = new RestTemplate();

    @PostMapping("/ask")
    public ResponseEntity<?> askQuestion(@RequestBody Map<String, String> request) {

        String question = request.get("question");

        String pythonApiUrl = "http://localhost:8000/ask"; // change later for Docker

        Map<String, String> body = new HashMap<>();
        body.put("question", question);

        ResponseEntity<AIResponse> response = restTemplate.postForEntity(
                pythonApiUrl,
                body,
                AIResponse.class
        );

        return ResponseEntity.ok(response.getBody());
        
    }
}