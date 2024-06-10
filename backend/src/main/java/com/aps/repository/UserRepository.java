package com.aps.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.aps.entity.User;

public interface UserRepository extends JpaRepository<User, Long> {

	User findByEmail(String email);
}