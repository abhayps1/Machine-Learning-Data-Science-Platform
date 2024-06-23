package com.aps.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.aps.entity.LoginRequest;
import com.aps.repository.LoginRepository;

@RestController
@RequestMapping("/api")
public class LoginController {

	@Autowired
	private LoginRepository loginRepository;

	@PostMapping("/login")
	public ResponseEntity<String> login(@RequestBody LoginRequest loginRequest) {
		String username = loginRequest.getUsername();
		String password = loginRequest.getPassword();

		LoginRequest userdetails = loginRepository.findByUsername(username);
		String user = userdetails.getUsername();
		String pass = userdetails.getPassword();

		// Validate username and password
		if (user.equals(username) && pass.equals(password)) {
			return ResponseEntity.ok("Login successful");
		} else {
			return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("Login failed");
		}
	}

}