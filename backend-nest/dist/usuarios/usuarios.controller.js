"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var __param = (this && this.__param) || function (paramIndex, decorator) {
    return function (target, key) { decorator(target, key, paramIndex); }
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.UsuariosController = void 0;
const common_1 = require("@nestjs/common");
const jsonwebtoken_1 = require("jsonwebtoken");
const common_2 = require("@nestjs/common");
const typeorm_1 = require("@nestjs/typeorm");
const typeorm_2 = require("typeorm");
const usuario_entity_1 = require("./usuario.entity");
const bcrypt = __importStar(require("bcryptjs"));
const jsonwebtoken_2 = require("jsonwebtoken");
let UsuariosController = class UsuariosController {
    usuarioRepo;
    constructor(usuarioRepo) {
        this.usuarioRepo = usuarioRepo;
    }
    async register(body) {
        const { nombre, apellido, email, password, dni, grado, descripcion, fecha_ingreso } = body;
        if (!nombre || !apellido || !email || !password) {
            return { ok: false, error: 'Faltan campos obligatorios.' };
        }
        const exists = await this.usuarioRepo.findOne({ where: { email } });
        if (exists) {
            return { ok: false, error: 'El correo ya está registrado.' };
        }
        const hashed = await bcrypt.hash(password, 10);
        const usuario = this.usuarioRepo.create({
            nombre, apellido, email, password: hashed, dni, grado, descripcion, fecha_ingreso
        });
        await this.usuarioRepo.save(usuario);
        return { ok: true };
    }
    async login(body) {
        const { username, password } = body;
        if (!username || !password) {
            return { error: 'Faltan datos.' };
        }
        const user = await this.usuarioRepo.findOne({ where: { email: username } });
        if (!user) {
            return { error: 'Correo o contraseña incorrectos.' };
        }
        const valid = await bcrypt.compare(password, user.password);
        if (!valid) {
            return { error: 'Correo o contraseña incorrectos.' };
        }
        const token = (0, jsonwebtoken_2.sign)({ id: user.id, email: user.email }, 'secreto', { expiresIn: '1d' });
        return { token, is_admin: false };
    }
    async me(req) {
        const auth = req.headers['authorization'];
        if (!auth || !auth.startsWith('Token '))
            throw new common_1.UnauthorizedException('No token');
        const token = auth.replace('Token ', '');
        let payload;
        try {
            payload = (0, jsonwebtoken_1.verify)(token, 'secreto');
        }
        catch {
            throw new common_1.UnauthorizedException('Token inválido');
        }
        const user = await this.usuarioRepo.findOne({ where: { id: payload.id } });
        if (!user)
            throw new common_1.UnauthorizedException('Usuario no encontrado');
        const { password, ...rest } = user;
        return rest;
    }
};
exports.UsuariosController = UsuariosController;
__decorate([
    (0, common_2.Post)('registro'),
    __param(0, (0, common_2.Body)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [Object]),
    __metadata("design:returntype", Promise)
], UsuariosController.prototype, "register", null);
__decorate([
    (0, common_2.Post)('login'),
    __param(0, (0, common_2.Body)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [Object]),
    __metadata("design:returntype", Promise)
], UsuariosController.prototype, "login", null);
__decorate([
    (0, common_1.Get)('me'),
    __param(0, (0, common_1.Req)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [Object]),
    __metadata("design:returntype", Promise)
], UsuariosController.prototype, "me", null);
exports.UsuariosController = UsuariosController = __decorate([
    (0, common_2.Controller)('api'),
    __param(0, (0, typeorm_1.InjectRepository)(usuario_entity_1.Usuario)),
    __metadata("design:paramtypes", [typeorm_2.Repository])
], UsuariosController);
//# sourceMappingURL=usuarios.controller.js.map