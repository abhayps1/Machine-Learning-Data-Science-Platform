package com.aps.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.aps.entity.LoginRequest;

@Repository
public interface LoginRepository extends JpaRepository<LoginRequest, String> {
	LoginRequest findByUsername(String username);
}
