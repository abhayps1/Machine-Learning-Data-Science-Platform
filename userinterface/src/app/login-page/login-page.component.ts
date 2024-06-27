import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClient }    from '@angular/common/http';
import { HttpClientModule } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login-page',
  standalone: true,
  imports: [FormsModule, HttpClientModule],
  templateUrl: './login-page.component.html',
  styleUrl: './login-page.component.css'
})
export class LoginPageComponent {
  username: string = "";
  password: string = "";

  constructor(private http : HttpClient, private router : Router){}

    signUp(){
      console.log("Your life is hell ! ")
      this.router.navigate(["../register"])
    }
  

  onSubmit(){
    const loginData = {
      username : this.username,
      password : this.password
    }

    this.http.post("https://localhost:8080/api/login", loginData)
    .subscribe(response => {
      console.log("Login Successful", response);
    }, error => {
      console.log("Login Failed with Error : ", error);
    }
    )
  }
}
