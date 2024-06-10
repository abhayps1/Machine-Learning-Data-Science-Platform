package com.aps.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.aps.entity.Role;

public interface RoleRepository extends JpaRepository<Role, Long> {
	Role findByName(String name);
}
