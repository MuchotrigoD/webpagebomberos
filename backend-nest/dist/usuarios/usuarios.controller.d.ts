import type { Request } from 'express';
import { Repository } from 'typeorm';
import { Usuario } from './usuario.entity';
export declare class UsuariosController {
    private readonly usuarioRepo;
    constructor(usuarioRepo: Repository<Usuario>);
    register(body: any): Promise<{
        ok: boolean;
        error: string;
    } | {
        ok: boolean;
        error?: undefined;
    }>;
    login(body: any): Promise<{
        error: string;
        token?: undefined;
        is_admin?: undefined;
    } | {
        token: string;
        is_admin: boolean;
        error?: undefined;
    }>;
    me(req: Request): Promise<{
        id: number;
        nombre: string;
        apellido: string;
        email: string;
        dni: string;
        grado: string;
        descripcion: string;
        fecha_ingreso: string;
        creado_en: Date;
    }>;
}
