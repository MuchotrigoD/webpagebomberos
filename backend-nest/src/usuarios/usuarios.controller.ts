import { Get, Req, UnauthorizedException } from '@nestjs/common';
import type { Request } from 'express';
import { verify } from 'jsonwebtoken';
import { Controller, Post, Body } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Usuario } from './usuario.entity';
import * as bcrypt from 'bcryptjs';
import { sign } from 'jsonwebtoken';

@Controller('api')
export class UsuariosController {
  constructor(
    @InjectRepository(Usuario)
    private readonly usuarioRepo: Repository<Usuario>,
  ) {}

  @Post('registro')
  async register(@Body() body: any) {
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

  @Post('login')
  async login(@Body() body: any) {
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
    // Simula un token (en producción usa JWT seguro y secreto fuerte)
    const token = sign({ id: user.id, email: user.email }, 'secreto', { expiresIn: '1d' });
    return { token, is_admin: false };
  }

  @Get('me')
  async me(@Req() req: Request) {
    const auth = req.headers['authorization'];
    if (!auth || !auth.startsWith('Token ')) throw new UnauthorizedException('No token');
    const token = auth.replace('Token ', '');
    let payload: any;
    try {
      payload = verify(token, 'secreto');
    } catch {
      throw new UnauthorizedException('Token inválido');
    }
    const user = await this.usuarioRepo.findOne({ where: { id: payload.id } });
    if (!user) throw new UnauthorizedException('Usuario no encontrado');
    // No enviar password
    const { password, ...rest } = user;
    return rest;
  }
}
