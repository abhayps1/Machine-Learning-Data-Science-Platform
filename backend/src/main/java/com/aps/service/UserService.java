package com.aps.service;

import com.aps.dto.UserDto;
import com.aps.entity.User;

public interface UserService {
	void saveUser(UserDto userDto);

	User findUserByEmail(String email);

	List<UserDto> findAllUsers();
}
