package com.aps.dto;

import org.hibernate.validator.constraints.NotEmpty;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class UserDto {
	private Long id;
	@NotEmpty
	private String firstName;
	@NotEmpty
	private String lastName;
	@NotEmpty(message = "Email should not be empty")
	@org.hibernate.validator.constraints.Email
	private String email;
	@NotEmpty(message = "Password should not be empty")
	private String password;
}
