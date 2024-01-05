<template>
    <nav class="navbar navbar-expand-md bg-success">
      <router-link to="/" class="navbar-brand fs-3 ms-3 text-secondary">ToBlog</router-link>
      <router-link to="/blog" class="navbar-brand fs-3 ms-3 text-info">Blog!:)</router-link>
      <router-link to="new-blog" class="nav-link mx-3 fs-4">New Blog!</router-link>
  
      <button class="navbar-toggler text-warning m-3" type="button" data-bs-toggle="collapse" data-bs-target="#btn">
        <i class="bi bi-body-text">T</i>
      </button>
      <div class="collapse navbar-collapse" id="btn">
        <template v-if=this.$store.state.user.isAuthenticated>
          <router-link to="/dashboard/my-account" class="btn btn-primary ms-auto mx-3">My Account</router-link>
        </template>
        <template v-else>
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <router-link to="login" class="btn btn-warning mx-4">login</router-link>
            </li>
            <li class="nav-item">
              <router-link to="sign-up" class="btn btn-primary mx-3">SignUp</router-link>
            </li>
          </ul>
            
        </template>
      </div>
    </nav>
  </template>
